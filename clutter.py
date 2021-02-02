import os
import time
import platform
import subprocess

from os import listdir
from pathlib import Path
from datetime import datetime

# Default: Two Million Seconds (3.30 Weeks)
RECENT = 2000000
locations = ["Downloads", "Desktop"]

# Command String
date_format = "%Y-%m-%d %H:%M:%S %z"
mac_added_template = ["mdls", "-name", "kMDItemDateAdded", "-raw"]

def mac_date_added(file_path):
  command = mac_added_template.copy()
  command.append(file_path)
  try:
    result = str(subprocess.check_output(command))[2:-1]
    result = datetime.strptime(result, date_format)
    return result.timestamp()
  except ValueError:
    return time.time()

def recently_used(file_path):
  most_recent = 0
  recent_time = time.time() - RECENT
  most_recent = max(most_recent, os.path.getmtime(file_path))
  most_recent = max(most_recent, os.path.getatime(file_path))
  most_recent = max(most_recent, os.path.getctime(file_path))
  if most_recent > recent_time:
    return True
  if platform.system() == "Darwin": # Mac OS
    return mac_date_added(file_path) > recent_time
  return True

def evaluate(folder):
  folder_path = str(Path.home() / folder)
  for f in listdir(folder_path):
    #print("  " + folder + "/" + f[:50])
    file_path = os.path.join(folder_path, f)
    if not recently_used(file_path):
      print("---- ARCHIVING: " + file_path[:60])
    #else:
      #print("++++ USED RECENTLY")

for folder in locations:
  print("Checking Folder: " + folder)
  evaluate(folder)
