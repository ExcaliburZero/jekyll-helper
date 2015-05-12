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

from locale import gettext as _

from gi.repository import Gio # pylint: disable=E0611

import os
import signal
import subprocess
from subprocess import Popen, PIPE
from subprocess import call, PIPE
from threading import Thread

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

        # Switches and Buttons
        self.directoryChooser =  self.builder.get_object("directoryChooser")
        self.serveSwitch = self.builder.get_object("serveSwitch")

    # General functions

    # Pull in program settings
    global settings
    settings = Gio.Settings("net.launchpad.jekyll-helper")

    # Set directory that stores the Jekyll website
    global site_directory
    site_directory = ""

    def set_website_directory(self, user_data):
        """Set the website's directory location."""
        print("Set Directory")
        global site_directory
        site_directory = self.directoryChooser.get_current_folder()
        print(site_directory)
        return;

    # Jekyll serve functions
    global is_serving
    is_serving = False

    global jekyll_serve

    def jekyll_serve_on(self):
        """Begin serving website through Jekyll."""
        global site_directory
        print("Jekyll Serve On: " + site_directory)

        # Get serve command from settings
        global settings
        print("Jekyll Serve Command: " + settings.get_string("serve-command"))
        args = [ settings.get_string("serve-command") ]
        print(args)

        # Serve website
        global jekyll_serve
        jekyll_serve = Popen(args, cwd=site_directory, shell=True, stdin=PIPE, stdout=PIPE, preexec_fn=os.setsid)
        global is_serving
        is_serving = True
        return;

    def jekyll_serve_off(self):
        """End serving website through Jekyll."""
        global jekyll_serve
        global site_directory
        print("Jekyll Serve Off: " + site_directory)
        os.killpg(jekyll_serve.pid, signal.SIGTERM)
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
