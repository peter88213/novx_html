"""Provide a class for HTML file representation based on template files.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_html
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from nvhtmlib.html_export import HtmlExport
from nvhtmlib.html_fop import read_html_file


class HtmlTemplatefileExport(HtmlExport):
    """Export content or metadata from a novelibre project to a HTML file.
    
    Public methods:
        write() -- write instance variables to the export file.
    
    Read the templates from external HTML flies.
    """

    # Reset default templates.
    _fileHeader = ''
    _partTemplate = ''
    _chapterTemplate = ''
    _sectionTemplate = ''
    _sectionDivider = ''
    _fileFooter = ''

    # Define template files.
    _HTML_HEADER = 'html_header'
    _CHARACTER_TEMPLATE = 'character_template'
    _LOCATION_TEMPLATE = 'location_template'
    _ITEM_TEMPLATE = 'item_template'
    _HTML_FOOTER = 'html_footer'
    _PART_TEMPLATE = 'part_template'
    _CHAPTER_TEMPLATE = 'chapter_template'
    _CHAPTER_END_TEMPLATE = 'chapter_end_template'
    _UNUSED_CHAPTER_TEMPLATE = 'unused_chapter_template'
    _UNUSED_CHAPTER_END_TEMPLATE = 'unused_chapter_end_template'
    _SCENE_TEMPLATE = 'section_template'
    _FIRST_SCENE_TEMPLATE = 'first_section_template'
    _UNUSED_SCENE_TEMPLATE = 'unused_section_template'
    _SECTION_DIVIDER = 'section_divider'
    _TEMPLATE_CHAPTER_TITLE = 'html templates'

    def __init__(self, filePath, **kwargs):
        """Read templates from files, if any.

        Positional arguments:
            filePath: str -- path to the file represented 
                             by the Novel instance.
            
        Required keyword arguments:
            template_path: str -- template directory path.
        
        Extends the superclass constructor.
        """

        def load_template(filePath):
            try:
                return read_html_file(filePath)
            except:
                return None

        super().__init__(filePath)
        templatePath = kwargs['template_path']

        # Project level.
        content = load_template(
            f'{templatePath}/'
            f'{self._HTML_HEADER}{self.EXTENSION}'
        )
        if content is not None:
            self._fileHeader = content
        content = load_template(
            f'{templatePath}/'
            f'{self._CHARACTER_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._characterTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._LOCATION_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._locationTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._ITEM_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._itemTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._HTML_FOOTER}{self.EXTENSION}'
        )
        if content is not None:
            self._fileFooter = content

        # Chapter level.
        content = load_template(
            f'{templatePath}/'
            f'{self._PART_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._partTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._CHAPTER_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._chapterTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._CHAPTER_END_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._chapterEndTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._UNUSED_CHAPTER_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._unusedChapterTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._UNUSED_CHAPTER_END_TEMPLATE}{self.EXTENSION}'
        )

        # Scene level.
        content = load_template(
            f'{templatePath}/'
            f'{self._SCENE_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._sectionTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._FIRST_SCENE_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._firstSceneTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._UNUSED_SCENE_TEMPLATE}{self.EXTENSION}'
        )
        if content is not None:
            self._unusedSceneTemplate = content
        content = load_template(
            f'{templatePath}/'
            f'{self._SECTION_DIVIDER}{self.EXTENSION}'
        )
        if content is not None:
            self._sectionDivider = content

    def _get_chapterMapping(self, chId, chapterNumber):
        """Return a mapping dictionary for a chapter section. 

        Positional arguments:
            chId: str -- chapter ID.
            chapterNumber: int -- chapter number.

        Extends the superclass method.
        """
        ROMAN = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        def number_to_roman(n):
            """Return n as a Roman number.
            
            Credit goes to the user 'Aristide' on stack overflow.
            https://stackoverflow.com/a/47713392
            """
            result = []
            for (arabic, roman) in ROMAN:
                (factor, n) = divmod(n, arabic)
                result.append(roman * factor)
                if n == 0:
                    break

            return "".join(result)

        TENS = {
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'
        }
        ZERO_TO_TWENTY = (
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten',
            'eleven',
            'twelve',
            'thirteen',
            'fourteen',
            'fifteen',
            'sixteen',
            'seventeen',
            'eighteen',
            'nineteen',
            'twenty'
        )

        def number_to_english(n):
            """Return n as a number written out in English.

            Credit goes to the user 'Hunter_71' on stack overflow.
            https://stackoverflow.com/a/51849443
            """
            if any(not x.isdigit() for x in str(n)):
                return ''

            if n <= 20:
                return ZERO_TO_TWENTY[n]

            elif n < 100 and n % 10 == 0:
                return TENS[n]

            elif n < 100:
                return (
                    f'{number_to_english(n - (n % 10))} '
                    f'{number_to_english(n % 10)}'
                )

            elif n < 1000 and n % 100 == 0:
                return (
                    f'{number_to_english(n / 100)} hundred'
                )

            elif n < 1000:
                return (
                    f'{number_to_english(n / 100)} hundred '
                    f'{number_to_english(n % 100)}'
                )

            elif n < 1000000:
                return (
                    f'{number_to_english(n / 1000)} thousand '
                    f'{number_to_english(n % 1000)}'
                )

            return ''

        chapterMapping = super()._get_chapterMapping(chId, chapterNumber)
        if chapterNumber:
            chapterMapping['ChNumberEnglish'] = number_to_english(
                chapterNumber
            ).capitalize()
            chapterMapping['ChNumberRoman'] = number_to_roman(
                chapterNumber
            )
        else:
            chapterMapping['ChNumberEnglish'] = ''
            chapterMapping['ChNumberRoman'] = ''
        return chapterMapping

