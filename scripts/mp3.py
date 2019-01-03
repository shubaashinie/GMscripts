import os
#import sys
import time
import re
import unittest,time

#from sys import argv
Iterations = 1 #argv[1] 

def Killmusic():
    os.system( "adb shell am force-stop com.google.android.music")

def Launchmusic():
    os.system( "adb shell am start -a android.intent.action.VIEW -d file:///SD card/Music/Yekkada Vunna.mp3 -t audio/mp3")
    os.system("adb shell input tap 339 1006")
    time.sleep(5)
    os.system("aadb shell input keyevent 121")
    os.system("adb shell dumpsys audio > aud.txt")
def launchvedio():
    os.system("adb shell am start -a android.intent.action.VIEW -d file:///mnt/sdcard/Nenlocal.mp4 -t video/mp4")
    os.system("adb shell dumpsys media.player > ved.txt")
    os.system("adb shell input tap 315 907")
Killmusic()
Launchmusic()
Killmusic()
#launchvedio()"""
