# tccutil
A macOS Permissions manager

You can use tccutil.py to manage an app's permissions (Microphone access, Camera access...)

Here are all disponible commands:
```
usage: tccutil.py [-h] [-e] [-d] [-r] [-id BUNDLEID] [-p APPPATH]
                  [-n APPNAME] [--contacts] [--calendars] [--reminders]
                  [--photos] [--camera] [--microphone]

optional arguments:
  -h, --help            show this help message and exit
  -e, --enable          Enable App Function
  -d, --disable         Disable App Function
  -r, --remove          Remove Record of App Function
  -id BUNDLEID, --bundleid BUNDLEID
                        Defines App Bundle ID
  -p APPPATH, --apppath APPPATH
                        Defines App Path to automatically find Bundle ID
  -n APPNAME, --appname APPNAME
                        Defines App Name to automatically find Bundle ID (if
                        app is not stored in /Applications/, please use
                        --apppath)
  --contacts            Change Contacts Access Status for the selected app
  --calendars           Change Calendars Access Status for the selected app
  --reminders           Change Reminders Access Status for the selected app
  --photos              Change Photos Access Status for the selected app
  --camera              Change Camera Access Status for the selected app
  --microphone          Change Microphone Access Status for the selected app
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
