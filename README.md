# tccutil
A macOS Permissions manager

You can use tccutil.py to manage an app's permissions (Microphone access, Camera access...)

Here are all disponible commands:
```
usage: tccutil.py [-h] [-e] [-d] [-id BUNDLEID] [-p APPPATH] [-n APPNAME]
                  [--contacts] [--calendar] [--reminders] [--photos]
                  [--camera] [--micro]

optional arguments:
  -h, --help            show this help message and exit
  -e, --enable          Enable App Function
  -d, --disable         Disable App Function
  -id BUNDLEID, --bundleid BUNDLEID
                        Defines App Bundle ID
  -p APPPATH, --apppath APPPATH
                        Defines App Path to automatically find Bundle ID
  -n APPNAME, --appname APPNAME
                        Defines App Name to automatically find Bundle ID (if
                        app is stored in /Applications/, else, please use
                        --apppath)
  --contacts            Change Contacts Access Status for the selected app
  --calendar            Change Calendar Access Status for the selected app
  --reminders           Change Reminders Access Status for the selected app
  --photos              Change Photos Access Status for the selected app
  --camera              Change Camera Status for the selected app
  --micro               Change Microphone Status for the selected app
```

## Add it to Path:

If you want to add it to your path (to be able to type ``tccutil`` without typing ``python /path/to/tccutil``)

Type the following commands in a terminal:
With zsh (macOS 10.15+):
```
PATHTOTCCUTIL="/path/to/tccutil.py"
echo "alias tccutil=python\ `echo $PATHTOTCCUTIL`" >> ~/.zshrc
```
Then restart Terminal for changes to take effect.
