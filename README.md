## PyAntiClutter
Organizes  old and unused files from MacOS Desktop & Downloads folder
(May be compatible with Windows)

#### Usage: python3 clutter.py

##### Set RECENT variable to the maximum number of seconds since a file has been:
- created
- modified
- added
- opened
- renamed
- previewed
Until the file is automatically moved into the directory's clutter folder.

EX:
- RECENT = 1200000    (2 weeks)
- RECENT = 1500000    (2 weeks 4 days)
- RECENT = 2000000    (3 weeks 2 days)
- RECENT = 5000000    (2 months)

##### To add directories beyond ~/Desktop and ~/Downloads, add the path to the locations array (from the home directory)

EX:
- locations = ["Downloads", "Desktop", "Desktop/School"]
- locations = ["Downloads", "Desktop", "dev"]
- locations = ["Downloads", "Desktop"]

##### To change the name of the created clutter folder, change:
CLUTTER_NAME = "Clutter"

Ex:
- CLUTTER_NAME = "Archive"
- CLUTTER_NAME = "old_stuff"
