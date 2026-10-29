"""Provide a class for HTML file representation.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_html
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from nvlib.model.file.file_export import FileExport
from nvhtmlib.novx_to_html import NovxToHtml


class HtmlExport(FileExport):
    """HTML file representation.
    
    Provide basic HTML templates for exporting chapters and sections.
    """
    DESCRIPTION = 'HTML export'
    EXTENSION = '.html'
    SCENE_DIVIDER = '* * *'

    _fileHeader = '''<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

<style type="text/css">
h1, h2, h3, h4, p {font: 1em monospace; margin: 3em; line-height: 1.5em}
h1, h2, h3, h4 {text-align: center}
h1 {letter-spacing: 0.5em; font-style: italic}
h1, h2 {font-weight: bold}
h3 {font-style: italic}
p {margin-top:0; margin-bottom:0}
p+p {margin-top:0; margin-bottom:0; text-indent: 1em}
p.title {text-align:center; font-weight:normal; text-transform: uppercase}
p.author {text-align:center; font-weight:normal}
p.sectiondivider {text-align:center; margin: 1.5em; line-height: 1.5em}
strong {font-weight:normal; text-transform: uppercase}
</style>

<title>$Title</title>
</head>

<body>
<p class=title><strong>$Title</strong></p>
<p class=author>by</p>
<p class=author>$AuthorName</p>

'''

    _partTemplate = '''<h1><a name="$ID" />$Title</h1>
'''

    _chapterTemplate = '''<h2><a name="$ID" />$Title</h2>
'''

    _sectionTemplate = '''<a name="$ID" /><!-- ${Title} -->
$SectionContent
'''

    _sectionDivider = f'<p class="sectiondivider">{SCENE_DIVIDER}</p>'

    _fileFooter = '''</body>
</html>
'''

    def _convert_from_novx(
            self,
            text,
            quick=False,
            firstInChapter=False,
            **kwargs
    ):
        """Return text, converted from *novelibre* markup to target format.
        
        Positional arguments:
            text -- string to convert.
        
        Optional arguments:
            quick: bool -- if True, apply a conversion mode for one-liners 
                           without formatting.
        
        Overrides the superclass method.
        """
        if not text:
            return ''

        if quick:
            return text.replace('\n', ' ')

        if text.lstrip().startswith('<'):
            # Remove all non-xhtml elements from the section content.
            parser = NovxToHtml()
            parser.feed(text, firstInChapter)
            return ''.join(parser.textList)

        newlines = []
        for line in text.split('\n'):
            newlines.append(f'<p>{line}</p>')
        return '\n'.join(newlines)

