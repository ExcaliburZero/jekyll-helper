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

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('jekyll_helper')

from jekyll_helper_lib import Window
from jekyll_helper.AboutJekyllHelperDialog import AboutJekyllHelperDialog
from jekyll_helper.PreferencesJekyllHelperDialog import PreferencesJekyllHelperDialog

# See jekyll_helper_lib.Window.py for more details about how this class works
class JekyllHelperWindow(Window):
    __gtype_name__ = "JekyllHelperWindow"

    # Initialize function
    def __init__(self):
        """Initialize the variables of the JekyllHelperWindow."""
        # Windows
        #self.AboutDialog = None # The window that contains information on the program
        #self.PreferencesDialog = None # The window that contains the preference settings

        # GUI elements
        #self.jekyllVersionLabel  # The label that gives the Jekyll version number
        #self.directoryChooser = None # The dropdown menu that allows the user to select the website directory
        #self.serveSwitch = None # The switch that allows the user to start and end the serving of the website
        #self.buildButton = None # The button that allows the user to build the website
        #self.pushButton = None  # The button that allows the user to push the website

        # Terminals
        self.jekyll_serve = None # Terminal to handle website serving
        self.jekyll_build = None # Terminal to run build command
        self.jekyll_push = None # Terminal to run push command

        # General variables
        self.site_directory = "" # The path of the website directory
        self.is_serving = False # If the site is currently being served or not

    # Initialization function
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(JekyllHelperWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutJekyllHelperDialog
        self.PreferencesDialog = PreferencesJekyllHelperDialog

        # Code for other initialization actions should be added here.

        ####
        # Initialization functions
        ####

        # Get user's version of Jekyll
        def get_jekyll_version():
            args = [ "jekyll -v" ]
            get_version = Popen(args, shell=True, stdin=PIPE, stdout=subprocess.PIPE)
            version = get_version.communicate()
            return version[0]

        ####
        # Text labels
        ####

        # Declare and set the Jekyll version label
        print("Version: " + str(get_jekyll_version()))
        self.jekyllVersionLabel = self.builder.get_object("jekyllVersionLabel")
        self.jekyllVersionLabel.set_text("Jekyll Version: " + str(get_jekyll_version()))

        ####
        # Switches and Buttons
        ####
        self.directoryChooser = self.builder.get_object("directoryChooser")
        self.serveSwitch = self.builder.get_object("serveSwitch")
        self.buildButton = self.builder.get_object("buildButton")
        self.pushButton = self.builder.get_object("pushButton")

    ####
    # General functions
    ####

    # Pull in program settings
    settings = Gio.Settings("net.launchpad.jekyll-helper")

    # Function to check if the set site directory exists
    def site_directory_exists(self, site_directory):
        """Check if the site directory that the user has chosen or not yet chosen exists."""
        # If no site directory has been entered
        if ( site_directory == "" ):
            return 1
        # If the chosen site directory does not exist
        elif ( os.path.exists(site_directory or "") == False ):
            return 2
        # If the chosen site directory does exist
        else:
            return 0

    # Set directory that stores the Jekyll website
    def set_website_directory(self, user_data):
        """Set the website's directory location."""
        print("Set Directory")
        self.site_directory = self.directoryChooser.get_current_folder()
        print(self.site_directory)
        # Check if the selected directory exists
        if (self.site_directory_exists(self.site_directory) == 1):
            print("No site directory has been entered.")
            return 1
        elif (self.site_directory_exists(self.site_directory) == 2):
            print("The entered directory does not exist.")
            return 2
        else:
            return 0

    # Jekyll serve functions
    def website_serve_on(self, site_directory):
        """Begin serving website through Jekyll."""
        print("Jekyll Serve On: " + site_directory)

        # Get serve command from settings
        print("Jekyll Serve Command: " + self.settings.get_string("serve-command"))
        args = [ self.settings.get_string("serve-command") ]
        print(args)

        # Serve website
        self.jekyll_serve = Popen(args, cwd=site_directory, shell=True, stdin=PIPE, stdout=PIPE, preexec_fn=os.setsid)
        self.is_serving = True
        return

    def website_serve_off(self, site_directory):
        """End serving website through Jekyll."""
        print("Jekyll Serve Off: " + site_directory)
        # End the serve command
        os.killpg(self.jekyll_serve.pid, signal.SIGTERM)
        self.is_serving = False
        return

    def on_serveSwitch_stateset(self, widget, state):
        """Begin or end serving website through Jekyll based on the serveSwitch value."""
        print("Serve: " + str(state))

        # Run the serve fuction if the site directory exists
        if (self.site_directory_exists(self.site_directory) == 0):
            if (state == True):
                self.website_serve_on(self.site_directory)
            elif (state == False):
                self.website_serve_off(self.site_directory)
            else:
                print("Error triggering Jekyll Serve")
            print("Is Serving: " + str(self.is_serving))
        elif (self.site_directory_exists(self.site_directory) == 1):
            print("No site directory has been entered.")
        elif (self.site_directory_exists(self.site_directory) == 2):
            print("The entered directory does not exist.")
        return

    # Jekyll build functions
    def website_build(self, site_directory):
        """Builds the website through Jekyll."""
        # Get build command from settings
        print("Jekyll Build Command: " + self.settings.get_string("build-command"))
        args = [ self.settings.get_string("build-command") ]
        print(args)

        # Build website
        self.jekyll_build = Popen(args, cwd=site_directory, shell=True, stdin=PIPE, stdout=PIPE, preexec_fn=os.setsid).wait()
        return

    def on_buildButton_clicked(self, widget):
        """Build the website when the build button is clicked."""
        print("Jekyll Build: " + self.site_directory)

        # Run the build fuction if the site directory exists
        if (self.site_directory_exists(self.site_directory) == 0):
            self.website_build(self.site_directory)
            print("Sucessfully built website")
        elif (self.site_directory_exists(self.site_directory) == 1):
            print("No site directory has been entered.")
        elif (self.site_directory_exists(self.site_directory) == 2):
            print("The entered directory does not exist.")
        return

    # Push website functions
    def website_push(self, site_directory):
        """Push the website using the user set push command."""
        # Get push command from settings
        print("Push Command: " + self.settings.get_string("push-command"))
        args = [ self.settings.get_string("push-command") ]
        print(args)

        # Push website
        self.jekyll_push = Popen(args, cwd=site_directory, shell=True, stdin=PIPE, stdout=PIPE, preexec_fn=os.setsid).wait()
        return

    def on_pushButton_clicked(self, widget):
        """Push the website when the push button is clicked."""
        print("Push: " + self.site_directory)

        # Run the push fuction if the site directory exists
        if (self.site_directory_exists(self.site_directory) == 0):
            self.website_push(self.site_directory)
            print("Sucessfully pushed website")
        elif (self.site_directory_exists(self.site_directory) == 1):
            print("No site directory has been entered.")
        elif (self.site_directory_exists(self.site_directory) == 2):
            print("The entered directory does not exist.")
        return
