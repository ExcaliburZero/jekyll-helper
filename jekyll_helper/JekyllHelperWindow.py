# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

import subprocess
from subprocess import call, PIPE
from threading import Thread

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('jekyll_helper')

from jekyll_helper_lib import Window
from jekyll_helper.AboutJekyllHelperDialog import AboutJekyllHelperDialog
from jekyll_helper.PreferencesJekyllHelperDialog import PreferencesJekyllHelperDialog

# Class for Jekyll serving
class JekyllServer(Thread):
    def __init__(self):
      Thread.__init__(self)

    # General functions

    # Safely run commands: written by Kilian for Trimage (MIT)
    def safe_call(self, command):
        """ cross-platform command-line check """
        while True:
            try:
                return call(command, shell=True, stdout=PIPE)
            except OSError as e:
                if e.errno == errno.EINTR:
                    continue
                else:
                    raise


    def start(self):
        self.safe_call("cd \"" + site_directory + "\"" + " && " + "jekyll serve")

    def end(self):
        self.safe_call("^C")

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

    # Safely run commands: written by Kilian for Trimage (MIT)
    def safe_call(self, command):
        """ cross-platform command-line check """
        while True:
            try:
                return call(command, shell=True, stdout=PIPE)
            except OSError as e:
                if e.errno == errno.EINTR:
                    continue
                else:
                    raise

    # Set directory that stores the Jekyll website
    global site_directory
    site_directory = ""

    def set_website_directory(self, user_data):
        """Set the website's directory location."""
        print("Set Directory")
        print(str(user_data))
        global site_directory
        site_directory = self.directoryChooser.get_current_folder()
        print(site_directory)
        return;

    # Jekyll serve functions
    global is_serving
    is_serving = False

    global j_serve
    j_serve = JekyllServer()

    def jekyll_serve_on(self):
        """Begin serving website through Jekyll."""
        global site_directory
        print("Jekyll Serve On: " + site_directory)
        global j_serve
        j_serve.start()
        global is_serving
        is_serving = True
        return;

    def jekyll_serve_off(self):
        """End serving website through Jekyll."""
        global site_directory
        print("Jekyll Serve Off: " + site_directory)
        global j_serve
        j_serve.end()
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
