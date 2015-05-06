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

        # Initialize serve switch
        self.serveSwitch = self.builder.get_object("serveSwitch")

    # Jekyll serve functions
    global is_serving
    is_serving = False

    def jekyll_serve_on(self):
        """Begin serving website through Jekyll"""
        print("Jekyll Serve On")
        global is_serving
        is_serving = True
        return;

    def jekyll_serve_off(self):
        """End serving website through Jekyll"""
        print("Jekyll Serve Off")
        global is_serving
        is_serving = False
        return;

    def on_serveSwitch_stateset(self, widget, state):
        """Begin or end serving website through Jekyll based on the serveSwitch value."""
        print("Serve: " + str(state))
        if (state == True):
            self.jekyll_serve_on();
        elif (state == False):
            self.jekyll_serve_off();
        else:
            print("Error triggering Jekyll Serve")
        print("Is Serving: " + str(is_serving))
        return;
