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

downloads="/Users/$USER/Downloads"
plist="com.captam3rica.timemachinescript.plist"
script="start_timemachine.sh"
launchd="$downloads/$plist"
s="$downloads/$script"
bin="/Users/$USER/bin"

# Cheching to see whether or not a bin directory exists in the users home folder
if [ ! -d "$bin" ]; then
    mkdir $bin
fi

# Moves the script and LaunchAgent to there respective locations
echo "Moving LaunchAgent to ~/Library/LaunchAgents"
cp $launchd /Users/$USER/Library/LaunchAgents/
echo "Moving start_timemachine.sh to ~/bin folder"
cp $s $bin

# Enabling the LaunchAgent
launchctl enable ~/Library/LaunchAgents/com.captam3rica.timemachine.plist


# Start the script for the first time
launchctl start com.captam3rica.timemachine
