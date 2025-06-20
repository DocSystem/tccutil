# tccutil

> **A macOS TCC permissions manager**

[![macOS](https://img.shields.io/badge/macOS-15.5-blue.svg)](https://www.apple.com/macos/)
[![Python](https://img.shields.io/badge/Python-3.6+-green.svg)](https://www.python.org/)

## 📋 Overview

✅ **Tested and verified on macOS 15.5 (Sequoia) plus other macOS versions**

⚠️ **Requires SIP to be [(at least partially)](#-notes) disabled**

🔧 **Supports all major TCC permission types**

## 🚨 Important Notice

> ⚠️ **WARNING**: This tool directly modifies the TCC.db file. Use at your own risk.

## 🎯 Supported Permissions

| Permission | Flag | Description |
|------------|------|-------------|
| 📇 **Contacts** | `--contacts` | Access to Contacts app data |
| 📅 **Calendars** | `--calendars` | Access to Calendar app data |
| ✅ **Reminders** | `--reminders` | Access to Reminders app data |
| 📸 **Photos** | `--photos` | Access to Photos library |
| 📹 **Camera** | `--camera` | Camera hardware access |
| 🎤 **Microphone** | `--microphone` | Microphone hardware access |
| 📍 **Location** | `--location` | Location Services access |
| 🖥️ **Screen Recording** | `--screen-recording` | Screen capture permissions |
| ♿ **Accessibility** | `--accessibility` | Accessibility API access |
| 💾 **Full Disk Access** | `--full-disk-access` | Complete file system access |
| ⌨️ **Input Monitoring** | `--input-monitoring` | Keystroke and input monitoring |
| 📶 **Bluetooth** | `--bluetooth` | Bluetooth hardware access |
| 🌐 **Local Network** | `--local-network` | Local network access |
| 🎵 **Media Library** | `--media-library` | Apple Music and media access |
| 🗣️ **Speech Recognition** | `--speech-recognition` | Speech recognition services |
| 🖥️ **Desktop Folder** | `--desktop-folder` | Desktop folder access |
| 📄 **Documents Folder** | `--documents-folder` | Documents folder access |
| 📥 **Downloads Folder** | `--downloads-folder` | Downloads folder access |

## 🛠️ Usage

### Basic Syntax

```bash
sudo python3 tccutil.py [ACTION] [APP_IDENTIFIER] [PERMISSION]
```

### Actions

- `-e, --enable` - Grant permission to the app
- `-d, --disable` - Deny permission to the app
- `-r, --remove` - Remove permission record entirely

### App Identification

- `-id BUNDLEID` - Specify app by bundle ID (e.g., `com.apple.Terminal`)
- `-p APPPATH` - Specify app by full path
- `-n APPNAME` - Specify app by name (searches in `/Applications/`)

## 📚 Example Commands

### Enable Permissions

```bash
# Grant Terminal full disk access
sudo python3 tccutil.py -e --full-disk-access -n Terminal

# Allow VS Code to record screen
sudo python3 tccutil.py -e --screen-recording -id com.microsoft.VSCode

# Grant camera access to Zoom
sudo python3 tccutil.py -e --camera -n zoom.us

# Enable microphone for Discord
sudo python3 tccutil.py -e --microphone -id com.hnc.Discord
```

### Disable Permissions

```bash
# Revoke location access from an app
sudo python3 tccutil.py -d --location -n "Some App"

# Disable contacts access
sudo python3 tccutil.py -d --contacts -id com.example.app
```

### Remove Permission Records

```bash
# Completely remove accessibility permission record
sudo python3 tccutil.py -r --accessibility -n "My App"

# Remove all traces of input monitoring permission
sudo python3 tccutil.py -r --input-monitoring -id com.example.keylogger
```

### Multiple Permissions

```bash
# Grant multiple permissions to an app
sudo python3 tccutil.py -e --camera --microphone --screen-recording -n "OBS Studio"
```

## 🔧 Installation & Setup

### Prerequisites

1. **Disable SIP** (System Integrity Protection):
   ```bash
   # Boot into Recovery Mode (⌘+R during startup)
   # Open Terminal and run:
   csrutil disable
   # Reboot normally
   ```

2. **Python 3.6+** (usually pre-installed on macOS)

### Quick Setup

1. **Clone or download** this repository
2. **Make executable**:
   ```bash
   chmod +x tccutil.py
   ```

### Add to PATH (Optional)

To use `tccutil` from anywhere:

```bash
# For zsh (macOS 10.15+)
echo 'alias tccutil="sudo python3 /path/to/tccutil.py"' >> ~/.zshrc
source ~/.zshrc

# For bash
echo 'alias tccutil="sudo python3 /path/to/tccutil.py"' >> ~/.bash_profile
source ~/.bash_profile
```

Then use it like:
```bash
tccutil -e --camera -n "My App"
```

## 📝 Notes

If you don't want to disable SIP completely for any reason.
The only protection that truly needs to be off is the filesystem protection.

The command that you'll need to run in recovery mode if you want this is:

```bash
csrutil enable --without fs
```
