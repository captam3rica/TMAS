#!/bin/bash

me=$USER
ADDRESS=$USER@kennesaw.edu
DATE=date

/usr/bin/tmutil startbackup
/usr/bin/tmutil destinationinfo >> /Users/$me/timemachine.log
echo "Backup has started" >> /Users/$me/timemachine.log
/bin/date >> /Users/$me/timemachine.log

# mail -s "iMac Backup Completed" $ADDRESS <<< "Backup has completed $DATE"
