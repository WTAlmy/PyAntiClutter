#!/bin/bash

clutterpath="/usr/local/bin/clutter.py"
cp clutter.py $clutterpath

(crontab -l; echo "30 12 * * * python3 $clutterpath") | crontab
