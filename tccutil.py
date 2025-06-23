#!/usr/bin/env python3

import sys
import os
import sqlite3
import plistlib
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--enable', help='Enable App Function', action='store_true')
parser.add_argument('-d', '--disable', help='Disable App Function', action='store_true')
parser.add_argument('-r', '--remove', help='Remove Record of App Function', action='store_true')
parser.add_argument('-id', '--bundleid', help='Defines App Bundle ID')
parser.add_argument('-p', '--apppath', help='Defines App Path to automatically find Bundle ID')
parser.add_argument('-n', '--appname', help='Defines App Name to automatically find Bundle ID (if app is stored in /Applications/, else, please use --apppath)')

services = {
    'contacts': ('kTCCServiceAddressBook', 'Contacts'),
    'calendars': ('kTCCServiceCalendar', 'Calendars'),
    'reminders': ('kTCCServiceReminders', 'Reminders'),
    'photos': ('kTCCServicePhotos', 'Photos'),
    'camera': ('kTCCServiceCamera', 'Camera'),
    'microphone': ('kTCCServiceMicrophone', 'Microphone'),
    'location': ('kTCCServiceLocation', 'Location Services'),
    'screen_recording': ('kTCCServiceScreenCapture', 'Screen Recording'),
    'accessibility': ('kTCCServiceAccessibility', 'Accessibility'),
    'full_disk_access': ('kTCCServiceSystemPolicyAllFiles', 'Full Disk Access'),
    'input_monitoring': ('kTCCServiceListenEvent', 'Input Monitoring'),
    'bluetooth': ('kTCCServiceBluetoothAlways', 'Bluetooth'),
    'local_network': ('kTCCServiceLocalNetwork', 'Local Network'),
    'media_library': ('kTCCServiceMediaLibrary', 'Media & Apple Music'),
    'speech_recognition': ('kTCCServiceSpeechRecognition', 'Speech Recognition'),
    'desktop_folder': ('kTCCServiceSystemPolicyDesktopFolder', 'Desktop Folder'),
    'documents_folder': ('kTCCServiceSystemPolicyDocumentsFolder', 'Documents Folder'),
    'downloads_folder': ('kTCCServiceSystemPolicyDownloadsFolder', 'Downloads Folder'),
}

for key, (_, name) in services.items():
    cli_arg = key.replace('_', '-')
    parser.add_argument(f'--{cli_arg}', dest=key, help=f'Change {name} Access Status for the selected app', action='store_true')

if len(sys.argv) == 1:
    parser.print_usage()
    parser.exit()
args = parser.parse_args()

tcc_db_path = os.path.abspath(os.path.expanduser('~/Library/Application Support/com.apple.TCC/TCC.db'))

def is_root():
    return os.geteuid() == 0

def read_plist(path):
    with open(path, 'rb') as plist_file:
        return plistlib.load(plist_file)

def modify_tcc_db(service, client, client_type, auth_value):
    with sqlite3.connect(tcc_db_path) as conn:
        cursor = conn.cursor()
        if auth_value < 0:
            cursor.execute(
                'DELETE FROM access WHERE service = ? AND client = ? AND client_type = ?;',
                (service, client, client_type)
            )
        else:
            cursor.execute(
                '''
                INSERT OR REPLACE INTO access
                (service, client, client_type, auth_value, auth_reason, auth_version, csreq,
                    policy_id, indirect_object_identifier_type, indirect_object_identifier,
                    indirect_object_code_identity, flags, last_modified)
                VALUES (?, ?, ?, ?, 0, 1, NULL, NULL, 0, 'UNUSED', NULL, 0, ?);
                ''',
                (service, client, client_type, auth_value, int(time.time()))
            )

def determine_bundle_id():
    if args.bundleid:
        return args.bundleid
    elif args.apppath:
        for sub in ['Contents/Info.plist', 'Info.plist']:
            info_plist_path = os.path.join(args.apppath, sub)
            if os.path.isfile(info_plist_path):
                print('Found a macOS app.' if 'Contents' in sub else 'Found an iOS app.')
                return read_plist(info_plist_path)['CFBundleIdentifier']
    elif args.appname:
        for sub in ['Contents/Info.plist', 'Info.plist']:
            path = f'/Applications/{args.appname}/{sub}'
            if os.path.isfile(path):
                print('Found a macOS app.' if 'Contents' in sub else 'Found an iOS app.')
                return read_plist(path)['CFBundleIdentifier']
    else:
        app_path = input('Drag the application here: ').strip().replace('\\', '\0').replace('\0\0', '\\').replace('\0', '')
        for sub in ['Contents/Info.plist', 'Info.plist']:
            path = os.path.join(app_path, sub)
            if os.path.isfile(path):
                print('Found a macOS app.' if 'Contents' in sub else 'Found an iOS app.')
                return read_plist(path)['CFBundleIdentifier']
    print('Could not locate a valid Info.plist')
    sys.exit(1)

if not is_root():
    print('You are not allowed to do this operation.')
    exit(1)

app_bundle_id = determine_bundle_id()

for action_flag, auth_value, action_text in [(args.enable, 2, 'Allowed'), (args.disable, 0, 'Disallowed'), (args.remove, -1, 'Removed')]:
    if action_flag:
        for key, (service, name) in services.items():
            if getattr(args, key):
                modify_tcc_db(service, app_bundle_id, 0, auth_value)
                print(f'{action_text} {"app access to" if auth_value == -1 else "the app to access"} {name}!')
