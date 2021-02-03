## PyAntiClutter
Organizes  old and unused files from MacOS Desktop & Downloads folder
(Possibly compatible with Windows)

## Usage: 
- Manual: ```python3 clutter.py```
- Automatic: ```bash autorun-unix.sh```

#### To increase or decrease the time until a file is archived:
Set RECENT to the maximum number of seconds since a file has been [created, modified, added, opened, renamed, or previewed] before it is automatically moved into the directory's clutter folder.
```
- RECENT = 1200000    (2 weeks)
- RECENT = 1500000    (2 weeks 4 days)
- RECENT = 2000000    (3 weeks 2 days)
- RECENT = 5000000    (2 months)
```
#### To add directories beyond ~/Desktop and ~/Downloads, add the path (from $HOME) to the locations array:
```
- locations = ["Downloads", "Desktop", "Desktop/School"]
- locations = ["Downloads", "Desktop", "dev"]
- locations = ["Downloads", "Desktop"]
```
#### To change the name of the created clutter folder, change the CLUTTER_NAME variable:
```
- CLUTTER_NAME = "Archive"
- CLUTTER_NAME = "old_stuff"
```

#### OS X 10.14+ Security/Compatability Note
MacOS may give a permissions error when running the script automatically when attempting to modify the Desktop or Downloads folders.
One possible solution would be to add "cron" to the Desktop/Downloads Folders & Files permission group in System Settings. See:
- https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/
