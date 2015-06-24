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

# This is your new dialog.

from gi.repository import Gio # pylint: disable=E0611

from locale import gettext as _

import os
import signal
from subprocess import Popen, PIPE

import logging
logger = logging.getLogger('jekyll_helper')

from jekyll_helper_lib.NewDialog import NewDialog

class NewJekyllHelperDialog(NewDialog):
    __gtype_name__ = "NewJekyllHelperDialog"

    # Initialize function
    def __init__(self):
        """Initialize the variables of the NewJekyllHelperWindow."""

        # GUI elements
        #self.website_name = None # The entry box for the new website name

        # Terminals
        self.jekyll_new = None # Terminal to create new Jekyll website

        # General variables
        self.is_newing = False # If a new site is currently being created or not

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the new dialog"""
        super(NewJekyllHelperDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.
        self.website_entry_box = self.builder.get_object('new_website_name_entry')
        self.directoryChooser = self.builder.get_object('directoryChooser')

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

    # Jekyll new functions
    def website_new(self, site_directory, site_name):
        """Create a new Jekyll website using the 'jekyll new' command."""
        args = [ "cd " + site_directory + " && " + self.settings.get_string("new-command1") + " " + site_name + " "  + self.settings.get_string("new-command2") ]
        self.is_newing = True
        self.jekyll_new = Popen(args, cwd=site_directory, shell=True, stdin=PIPE, stdout=PIPE, preexec_fn=os.setsid).wait()
        print("Created new website named " + self.website_name)
        self.is_newing = False
        # Close the new website window
        self.destroy()
        return

    def on_createButton_clicked(self, widget):
        """Create a new Jekyll website when the new menu entry has been clicked."""
        # Create the new website if the specified directory exists
        self.site_directory = self.directoryChooser.get_current_folder()
        self.website_name = self.website_entry_box.get_text()
        if ((self.site_directory_exists(self.site_directory) == 0) and (self.website_name != "")):
            self.website_new(self.site_directory, self.website_name)
        return

    # Close windo when Cancel button is clicked
    def on_cancelButton_clicked(self, widget):
        """Close the new website window when the cancel button has been clicked."""
        # Close the new website window
        self.destroy()

    # Close window and cleanup excess variables
    def on_destroy(self, widget, data=None):
        """Cleanup and remove unwanted variables when the new website window is closed."""
        # Destroy all running terminals
        if (self.is_newing == True): # Kill new terminal if it is still running
            os.killpg(self.jekyll_new.pid, signal.SIGTERM)
            self.is_newing = False
