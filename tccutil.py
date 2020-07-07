import os
from plistlib import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--enable", help="Enable App Function", action="store_true")
parser.add_argument("-d", "--disable", help="Disable App Function", action="store_true")
parser.add_argument("-id", "--bundleid", help="Defines App Bundle ID")
parser.add_argument("-p", "--apppath", help="Defines App Path to automatically find Bundle ID")
parser.add_argument("-n", "--appname", help="Defines App Name to automatically find Bundle ID (if app is stored in /Applications/, else, please use --apppath)")
parser.add_argument("--contacts", help="Change Contacts Access Status for the selected app", action="store_true")
parser.add_argument("--calendar", help="Change Calendar Access Status for the selected app", action="store_true")
parser.add_argument("--reminders", help="Change Reminders Access Status for the selected app", action="store_true")
parser.add_argument("--photos", help="Change Photos Access Status for the selected app", action="store_true")
parser.add_argument("--camera", help="Change Camera Status for the selected app", action="store_true")
parser.add_argument("--micro", help="Change Microphone Status for the selected app", action="store_true")
#parser.add_argument("--accessibility", help="Change Contacts Access Status for the selected app", action="store_true")
args = parser.parse_args()
if args.enable:
    if args.bundleid:
        appBundleId = args.bundleid
    elif args.apppath:
        appPlist = readPlist(args.apppath + "/Contents/Info.plist")
        appBundleId = appPlist["CFBundleIdentifier"]
    elif args.appname:
        appPlist = readPlist("/Applications/" + args.appname + ".app/Contents/Info.plist")
        appBundleId = appPlist["CFBundleIdentifier"]
    else:
        appPath = input("Glissez l'application ici : ").strip()
        appPlist = readPlist(appPath + "/Contents/Info.plist")
        appBundleId = appPlist["CFBundleIdentifier"]

    os.system("sudo echo")

    if args.contacts:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"INSERT or REPLACE INTO access VALUES('kTCCServiceAddressBook','" + appBundleId + "',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1551892126);\"")
        print("Allowed the app to access Contacts!")
        print(" ")
    if args.calendar:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"INSERT or REPLACE INTO access VALUES('kTCCServiceCalendar','" + appBundleId + "',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1551892126);\"")
        print("Allowed the app to access Calendar!")
        print(" ")
    if args.reminders:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"INSERT or REPLACE INTO access VALUES('kTCCServiceReminders','" + appBundleId + "',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1551892126);\"")
        print("Allowed the app to access Reminders!")
        print(" ")
    if args.photos:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"INSERT or REPLACE INTO access VALUES('kTCCServicePhotos','" + appBundleId + "',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1551892126);\"")
        print("Allowed the app to access Photos!")
        print(" ")
    if args.camera:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"INSERT or REPLACE INTO access VALUES('kTCCServiceCamera','" + appBundleId + "',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1551892126);\"")
        print("Allowed the app to access Camera!")
        print(" ")
    if args.micro:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"INSERT or REPLACE INTO access VALUES('kTCCServiceMicrophone','" + appBundleId + "',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1551892126);\"")
        print("Allowed the app to access Microphone!")
        print(" ")
    #if args.accessibility:
    #    os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"INSERT or REPLACE INTO access VALUES('kTCCServiceAccessibility','" + appBundleId + "',0,1,1,NULL,NULL,NULL,'UNUSED',NULL,0,1551892126);\"")
    #    print("Allowed the app to access Accessibility!")
    #    print(" ")
if args.disable:
    if args.bundleid:
        appBundleId = args.bundleid
    elif args.apppath:
        appPlist = readPlist(args.apppath + "/Contents/Info.plist")
        appBundleId = appPlist["CFBundleIdentifier"]
    elif args.appname:
        appPlist = readPlist("/Applications/" + args.appname + ".app/Contents/Info.plist")
        appBundleId = appPlist["CFBundleIdentifier"]
    else:
        appPath = input("Glissez l'application ici : ").strip()
        appPlist = readPlist(appPath + "/Contents/Info.plist")
        appBundleId = appPlist["CFBundleIdentifier"]

    os.system("sudo echo")

    if args.contacts:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"DELETE FROM access WHERE service = 'kTCCServiceAddressBook' AND client = '" + appBundleId + "';\"")
        print("Removed app access to the Contacts!")
        print(" ")
    if args.calendar:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"DELETE FROM access WHERE service = 'kTCCServiceCalendar' AND client = '" + appBundleId + "';\"")
        print("Removed app access to the Calendar!")
        print(" ")
    if args.reminders:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"DELETE FROM access WHERE service = 'kTCCServiceReminders' AND client = '" + appBundleId + "';\"")
        print("Removed app access to the Reminders!")
        print(" ")
    if args.photos:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"DELETE FROM access WHERE service = 'kTCCServicePhotos' AND client = '" + appBundleId + "';\"")
        print("Removed app access to the Photos!")
        print(" ")
    if args.camera:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"DELETE FROM access WHERE service = 'kTCCServiceCamera' AND client = '" + appBundleId + "';\"")
        print("Removed app access to the Camera!")
        print(" ")
    if args.micro:
        os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"DELETE FROM access WHERE service = 'kTCCServiceMicrophone' AND client = '" + appBundleId + "';\"")
        print("Removed app access to the Microphone!")
        print(" ")
    #if args.accessibility:
    #    os.system("sudo sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \"DELETE FROM access WHERE service = 'kTCCServiceAccessibility' AND client = '" + appBundleId + "';\"")
    #    print("Removed app access to the Accessibility!")
    #    print(" ")
