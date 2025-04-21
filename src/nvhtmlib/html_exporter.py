"""Provide a class for novelibre to HTML conversion.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_html
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from nvhtmlib.html_templatefile_export import HtmlTemplatefileExport
from nvlib.model.converter.converter import Converter
from nvhtmlib.export_any_target_factory import ExportAnyTargetFactory
from nvlib.model.novx.novx_file import NovxFile


class HtmlExporter(Converter):
    """A converter class for html export.

    Class constants:
        EXPORT_SOURCE_CLASSES -- List of YwFile subclasses from which can be exported.
        EXPORT_TARGET_CLASSES -- List of FileExport subclasses to which export is possible.
    """
    EXPORT_SOURCE_CLASSES = [NovxFile]
    EXPORT_TARGET_CLASSES = [HtmlTemplatefileExport]

    def __init__(self):
        """Extends the superclass constructor.

        Delegate the exportTargetFactory to a project
        specific class that accepts all suffixes.
        Extends the superclass constructor.
        """
        super().__init__()
        self.exportTargetFactory = ExportAnyTargetFactory(self.EXPORT_TARGET_CLASSES)

