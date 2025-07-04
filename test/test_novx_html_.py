"""Regression test for the novx_html project.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_html
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import unittest
import novx_html_
from shutil import copyfile

# Test environment

# The paths are relative to the "test" directory,
# where this script is placed and executed

TEST_PATH = os.getcwd() + '/../test'
TEST_DATA_PATH = TEST_PATH + '/data/'
TEST_EXEC_PATH = TEST_PATH + '/temp/'
TEMPLATE_PATH = '../../sample/'

# To be placed in TEST_DATA_PATH:

# Test data
NOVX_NORMAL = 'normal.novx'
PAPERBACK = 'normal_paperback.html'
SECTIONLIST = 'normal_sectionlist.html'
SCRIPT = 'normal_manuscript.html'
CHARAS = 'normal_characters.html'
LOCS = 'normal_locations.html'


def read_file(inputFile):
    try:
        with open(inputFile, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        # HTML files exported by a word processor may be ANSI encoded.
        with open(inputFile, 'r') as f:
            return f.read()


def remove_all_testfiles():
    try:
        os.remove(TEST_EXEC_PATH + NOVX_NORMAL)
    except:
        pass
    try:
        os.remove(TEST_EXEC_PATH + SECTIONLIST)
    except:
        pass
    try:
        os.remove(TEST_EXEC_PATH + SCRIPT)
    except:
        pass
    try:
        os.remove(TEST_EXEC_PATH + CHARAS)
    except:
        pass
    try:
        os.remove(TEST_EXEC_PATH + LOCS)
    except:
        pass
    try:
        os.remove(TEST_EXEC_PATH + PAPERBACK)
    except:
        pass


class NormalOperation(unittest.TestCase):
    """Test case: Normal operation."""

    def setUp(self):
        os.makedirs(TEST_EXEC_PATH, exist_ok=True)
        remove_all_testfiles()
        copyfile(TEST_DATA_PATH + NOVX_NORMAL, TEST_EXEC_PATH + NOVX_NORMAL)

    def test_sectionlist(self):
        os.chdir(TEST_EXEC_PATH)
        novx_html_.run(TEST_EXEC_PATH + NOVX_NORMAL, TEMPLATE_PATH +
                     'sectionlist', '_sectionlist', True)
        self.assertEqual(read_file(TEST_EXEC_PATH + SECTIONLIST),
                         read_file(TEST_DATA_PATH + SECTIONLIST))

    def test_script(self):
        os.chdir(TEST_EXEC_PATH)
        novx_html_.run(TEST_EXEC_PATH + NOVX_NORMAL, TEMPLATE_PATH +
                     'manuscript', '_manuscript', True)
        self.assertEqual(read_file(TEST_EXEC_PATH + SCRIPT),
                         read_file(TEST_DATA_PATH + SCRIPT))

    def test_characters(self):
        os.chdir(TEST_EXEC_PATH)
        novx_html_.run(TEST_EXEC_PATH + NOVX_NORMAL, TEMPLATE_PATH +
                     'characters', '_characters', True)
        self.assertEqual(read_file(TEST_EXEC_PATH + CHARAS),
                         read_file(TEST_DATA_PATH + CHARAS))

    def test_locations(self):
        os.chdir(TEST_EXEC_PATH)
        novx_html_.run(TEST_EXEC_PATH + NOVX_NORMAL, TEMPLATE_PATH +
                     'locations', '_locations', True)
        self.assertEqual(read_file(TEST_EXEC_PATH + LOCS),
                         read_file(TEST_DATA_PATH + LOCS))

    def tearDown(self):
        remove_all_testfiles()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
