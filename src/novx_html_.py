"""Export novelibre project to HTML.

Version @release
Requires Python 3.6+
Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_html
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or 
(at your option) any later version.

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.
"""
import os
import argparse
from nvlib.user_interface.ui import Ui
from nvlib.user_interface.ui_cmd import UiCmd
from nvhtmlib.html_exporter import HtmlExporter


def run(sourcePath, templatePath, suffix, silentMode=True):
    if silentMode:
        ui = Ui('')
    else:
        ui = UiCmd('Export html from novelibre')
    converter = HtmlExporter()
    converter.ui = ui
    kwargs = {'suffix': suffix, 'template_path': templatePath}
    converter.run(sourcePath, **kwargs)
    ui.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Export novelibre project to html.',
        epilog='If no template directory is set, templates are searched for in the novelibre project directory. If no templates are found, the output file will be empty.')
    parser.add_argument('sourcePath', metavar='Project',
                        help='novelibre project file')
    parser.add_argument('-t', dest='templatePath', metavar='template-dir',
                        help='path to the directory containing the templates')
    parser.add_argument('-s', dest='suffix', metavar='suffix',
                        help='suffix to the output file name (optional)')
    parser.add_argument('--silent',
                        action="store_true",
                        help='suppress error messages and the request to confirm overwriting')
    args = parser.parse_args()
    if args.templatePath:
        templatePath = args.templatePath
    else:
        templatePath = os.path.dirname(args.sourcePath)
    if args.templatePath is not None:
        templatePath = args.templatePath
    else:
        templatePath = os.path.dirname(args.sourcePath)
    if not templatePath:
        templatePath = '.'
    if args.suffix is not None:
        suffix = args.suffix
    else:
        suffix = ''
    run(args.sourcePath, templatePath, suffix, args.silent)
