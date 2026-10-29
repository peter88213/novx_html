"""Provide a class for parsing novx section content, converting it to HTML.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_html
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from xml import sax


class NovxToHtml(sax.ContentHandler):
    """A parser to convert novx markup to HTML."""
    NON_HTML = ('comment', 'note')

    def __init__(self):
        super().__init__()
        self.textList = None
        self._skip = None
        self._firstParagraphInChapter = None

    def feed(self, xmlString, firstInChapter):
        """Feed a string file to the parser.
        
        Positional arguments:
            filePath: str -- novx document path.        
        """
        self._firstParagraphInChapter = firstInChapter
        xmlString = f'<novx>{xmlString}</novx>'
        self.textList = []
        if xmlString:
            self._skip = False
            sax.parseString(xmlString, self)

    def characters(self, content):
        """Receive notification of character data.
        
        Overrides the xml.sax.ContentHandler method             
        """
        if self._skip:
            return

        self.textList.append(content)

    def endElement(self, name):
        """Signals the end of an element in non-namespace mode.
        
        Overrides the xml.sax.ContentHandler method     
        """
        if name == 'novx':
            return

        if name in self.NON_HTML:
            self._skip = False
            return

        if self._skip:
            return

        self.textList.append(f'</{name}>')

    def startElement(self, name, attrs):
        """Signals the start of an element in non-namespace mode.
        
        Overrides the xml.sax.ContentHandler method             
        """
        if name == 'novx':
            return

        if name in self.NON_HTML:
            self._skip = True
            return

        if self._skip:
            return

        htmlAttributes = []
        for attribute in attrs.items():
            attrKey, attrValue = attribute
            htmlAttributes.append(f'{attrKey}="{attrValue}"')
        if htmlAttributes:
            self.textList.append(f"<{name} {' '.join(htmlAttributes)}>")
        elif name == 'p' and self._firstParagraphInChapter:
            self.textList.append('<p class="ChpStart">')
            self._firstParagraphInChapter = False
        else:
            self.textList.append(f'<{name}>')

