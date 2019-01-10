#!/bin/bash

#################################################
#################################################
# NOTICE: DO NOT USE - STILL A WORK IN PROGRESS #
#################################################
#################################################

# Installation script for TMAS

#### TO DO ####
# 1. Check to see if TM is configured
# 2. Enable TM setup through script
# 3. Check to make sure that backup disk is mounted
# 4. Port to python

#################################################

# Ask for sudo privilages from the start
sudo -v

# Keep-alive: update existing `sudo` time stamp until `.osx` has finished
while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

### Variables
downloads="/Users/$USER/Downloads"
plist="com.captam3rica.timemachinescript.plist"
script="start_timemachine.sh"
launchd="$downloads/$plist"
s="$downloads/$script"
bin="/usr/local/bin"

# Moves the script and LaunchAgent to there respective locations
echo "Moving LaunchAgent to ~/Library/LaunchAgents"
cp $launchd /Users/$USER/Library/LaunchAgents/
echo "Moving start_timemachine.sh to /usr/local/bin folder"
sudo cp $s $bin

### Check the time machine status
sudo tmutil --status

### Configure timemachine if needed
if [[ condition ]]; then
  #statements
else
  #do something else 
fi

# Enabling the LaunchAgent
sudo launchctl enable \
/Users/$USERS/Library/LaunchAgents/com.captam3rica.timemachine.plist

# Start the script for the first time
sudo launchctl start com.captam3rica.timemachine
