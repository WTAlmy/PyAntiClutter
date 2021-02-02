import os
import time
import ntpath
import platform
import subprocess

from os import listdir
from pathlib import Path
from datetime import datetime

# Default: Two Million Seconds (2.48 Weeks)
RECENT = 1200000
CLUTTER_NAME = "Clutter"
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
  return False


def archive(source_folder, files_list):
  clutter_path = os.path.join(source_folder, CLUTTER_NAME)
  if not os.path.exists(clutter_path):
    os.makedirs(clutter_path)
  if os.path.isdir(clutter_path):
    for f_path in files_list:
      try:
        print("-- ARCHIVING: " + f_path[:65])
        f_name = ntpath.basename(f_path)
        os.rename(f_path, os.path.join(clutter_path, f_name))
      except OSError as e:
        print("OSError: " + f_path)
        print(e)

def evaluate(folder):
  folder_path = str(Path.home() / folder)
  unused_items = []
  for f in listdir(folder_path):
    file_path = os.path.join(folder_path, f)
    if not recently_used(file_path):
      if os.path.isfile(file_path):
          unused_items.append(file_path)
  if (len(unused_items) > 0):
    archive(folder_path, unused_items)
  else:
    print("-- All clean")


for folder in locations:
  print("Checking Folder: " + folder)
  evaluate(folder)
