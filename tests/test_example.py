#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2015 <Christopher Wells> <cwellsny@nycap.rr.com>
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
### END LICENSE

import sys
import os.path
import unittest
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from jekyll_helper import AboutJekyllHelperDialog
from jekyll_helper import JekyllHelperWindow

class TestExample(unittest.TestCase):
    def setUp(self):
        self.AboutJekyllHelperDialog_members = [
        'AboutDialog', 'AboutJekyllHelperDialog', 'gettext', 'logger', 'logging']

    def test_AboutJekyllHelperDialog_members(self):
        all_members = dir(AboutJekyllHelperDialog)
        public_members = [x for x in all_members if not x.startswith('_')]
        public_members.extend(['gettext'])
        public_members.sort()
        self.assertEqual(self.AboutJekyllHelperDialog_members, public_members)

# Test the site directory check function
class TestCheckSiteDirectory(unittest.TestCase):
    """Tests the site directory checking function to make sure that it works properly."""
    def setUp(self):
        self.prog_window = JekyllHelperWindow.JekyllHelperWindow()

    def test_site_directory_exists(self):
        self.assertEqual(self.prog_window.site_directory_exists(os.getcwd()), 0)    # Check current directory
        self.assertEqual(self.prog_window.site_directory_exists(""), 1) # Check a blank directory
        self.assertEqual(self.prog_window.site_directory_exists(os.getcwd() + "htrjek"), 2) # Check a nonexistant directory

if __name__ == '__main__':
    unittest.main()
