#!/bin/bash

clutterpath="/usr/local/bin/clutter.py"
cp clutter.py $clutterpath

# Runs daily at 12:30pm
(crontab -l; echo "30 12 * * * python3 $clutterpath") | crontab
