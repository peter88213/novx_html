"""Build the novx_html application package.
        
Note: VERSION must be updated manually before starting this script.

For further information see https://github.com/peter88213/novx_html
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from shutil import copy2
from shutil import make_archive
from shutil import rmtree
import sys

sys.path.insert(0, f'{os.getcwd()}/../../novelibre/tools')
from package_builder import PackageBuilder

VERSION = '0.5.0'


class ApplicationBuilder(PackageBuilder):

    PRJ_NAME = 'novx_html'
    LOCAL_LIB = 'nvhtmlib'

    def __init__(self, version):
        super().__init__(version)
        self.sourceFile = f'{self.sourceDir}{self.PRJ_NAME}_.py'
        self.distFiles = [
            (self.testFile, self.buildDir),
            ('../LICENSE', self.buildDir),
        ]

    def add_extras(self):
        self.add_icons()
        self.add_sample()

    def create_pyz(self, sourceDir, targetDir, release):
        return

    def make_zip(self, sourceDir, targetDir, release):
        """Create the alternative zip file.
        
        Overrides the superclass method.
        """
        self.write_setup_script(sourceDir)
        copy2('../docs/help/index.md', f'{sourceDir}/README.md')
        target = f'{targetDir}/{release}'
        print(f'Writing "{target}.zip" ...')
        make_archive(target, 'zip', sourceDir)

    def prepare_package(self):
        """Create the package directory and populate it with the basic files."""
        print(f'\nProviding empty "{self.buildDir}" ...')
        try:
            rmtree(self.buildBase)
        except FileNotFoundError:
            pass
        self.collect_dist_files(self.distFiles)

    def write_setup_script(self, filePath):
        return


def main():
    ab = ApplicationBuilder(VERSION)
    ab.run()


if __name__ == '__main__':
    main()

