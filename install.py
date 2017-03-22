#!/usr/bin/python2

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
import Tkinter

# Variablas

user_name = os.environ["USER"]
os_name = os.uname()
downloads = "/Users/user_name/Downloads"
plist_file = "com.captam3rica.timemachinescript.plist"
start_script = "start_timemachine.sh"
la = "downloads/plist_file"
sl = 'downloads/start_script'
# directory = "/Users/jwils156/bin"
# directory = "/home/captam3rica/bin/"

# window = Tkinter
# win.size("600x200")

# Is TimeMachine configured
# If not, configure TimeMachine

# Is the backup disk mounted
# If not, ask user to attach disk

# Check for OS (Mac OS, Linux, etc ...)
if os_name == 'Darwin':
    directory = "/Users/jwils156/bin"
else:
    directory = "/home/captam3rica/bin"
    print os_name


# Check for a bin folder
# If bin does not exit, create it
def does_path_exist(directory):
    bin_dir = os.path.dirname(directory)
    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)
    else:
        print "bin exists"


print does_path_exist(directory)
