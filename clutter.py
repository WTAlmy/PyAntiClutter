import os
from os import listdir
from pathlib import Path

locations = ["Downloads", "Desktop"]

def evaluate(folder):
  f_path = str(Path.home() / folder)
  for f in listdir(f_path):
    print("  " + folder + "/" + f[:50])

for folder in locations:
  print("Checking Folder: " + folder)
  evaluate(folder)
