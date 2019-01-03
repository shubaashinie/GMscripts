import os
import sys
import time
import re
import unittest,time

#Before running scripts make sure whatsapp is installed and has a contact with name mentioned in config file
print("=======================================================================")
print("Wifi enable disable test started")
print("=======================================================================")
from sys import argv
Iterations = 1 

def Killwhatsapp():
    os.system( "adb shell am force-stop com.whatsapp")

def Launchwhatsapp():
    os.system( "adb shell am start -n com.whatsapp/
               .Main")
def Whatsapp_searchcontact():
    #coordinates to touch search 
    #os.system( "adb shell input tap 601 106")
    time.sleep(5)
    os.system("adb shell input keyevent 84")
    time.sleep(2)
    os.system( "adb shell input text Anitha")
    time.sleep(2)
    #coordinates to touch 1st contact displayed after search 
    os.system( "adb shell input tap 354 313")
def Whatsapp_sendmessage():   
    os.system( "adb shell input text hii")
    os.system( "adb shell input tap 651 777")
"""
def forward():
    os.system("adb shell input touchscreen swipe 127 1141 127 1141 1000")
    os.system("adb shell input keyevent 674 115")
    os.system("adb shell input keyevent 624 1212")
    """
# Killing whatsapp to make sure home screen is launched while launching
Killwhatsapp()
Launchwhatsapp()
Whatsapp_searchcontact()
for n in range(int(Iterations)):
    Whatsapp_sendmessage()
    n+1
#forward()    
