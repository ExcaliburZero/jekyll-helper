# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('jekyll_helper')

from jekyll_helper_lib import Window
from jekyll_helper.AboutJekyllHelperDialog import AboutJekyllHelperDialog
from jekyll_helper.PreferencesJekyllHelperDialog import PreferencesJekyllHelperDialog

# See jekyll_helper_lib.Window.py for more details about how this class works
class JekyllHelperWindow(Window):
    __gtype_name__ = "JekyllHelperWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(JekyllHelperWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutJekyllHelperDialog
        self.PreferencesDialog = PreferencesJekyllHelperDialog

        # Code for other initialization actions should be added here.

