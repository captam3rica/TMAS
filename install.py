#!/usr/bin/python

"""
Installation script for TimeMachine Automation Script (TMAS)

Checks to see if a local user "bin" directory exists. If not, the script
will create it. Then, the .plist and start_timemachine.sh files are
moved to there respective locations from the current user's downloads
folder (or wherever there Mac puts their downloads)

Next, the script checks to see if TimeMachine is configured on the
user's computer already, and if the users's backup disk is mounted and
available. If TimeMachine is not configured, the user will be walked
through the setup process.

Finally, the install script will attempt to start time machine for the
first time to get an initial backup.
"""

# Modules
import os
import sys
import subprocess
import Tkinter

# Variablas

user_name = os.environ["USER"]
downloads = "/Users/%s/Downloads" % user_name
plist_file = "com.captam3rica.timemachinescript.plist"
start_timemachine = "start_timemachine.sh"
launch_agent = "downloads/%s" % plist_file
script_location = 'downloads/%s' % start_timemachine

# window = Tkinter
# win.size("600x200")

# Check for OS (Mac OS, Linux, etc ...)
if sys.platform == 'darwin':
    directory = '/Users/%s/bin/' % user_name
    print "Mac OS"
    print user_name
else:
    directory = "/home/captam3rica/bin"
    print "Linux"


# Is TimeMachine configured
# If not, configure TimeMachine
def timemachine_conf(self):
    self.time_machine = subprocess.Popen("tmutil --status")
    self.backup_drive =  # this could look for a list of attached drives
    if self.time_machine:
        print "No need to configure TimeMachine"
    else:
        print "TimeMachine needs to be setup"
        subprocess.Popen("tmutil %s" % self.backup_drive)

# Is the backup disk mounted
# If not, ask user to attach disk


# Check for a bin folder
# If bin does not exit, create it
def does_path_exist(directory):
    bin_dir = os.path.dirname(directory)
    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)
    else:
        print "bin exists"


print does_path_exist(directory)
