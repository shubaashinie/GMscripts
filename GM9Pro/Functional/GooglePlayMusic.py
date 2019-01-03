    
import os
from time import sleep
def LaunchGooglePlayMusic():
    os.system("adb shell monkey -p com.google.android.music -c android.intent.category.LAUNCHER  1")
    sleep(3)
def Activity():
    os.system("adb shell input tap 524 168")
    os.system("adb shell input text a%sthousand%syears")
    os.system("adb shell input keyevent 66")
    for i in range(0,3):
        os.system("adb shell input keyevent 20")
    os.system("adb shell input keyevent 66")
    for i in range(0,2):
        sleep(3)
        os.system("adb shell input tap 975 536")
    
def KillGooglePlayMusic():
    os.system("adb shell am force-stop com.google.android.music")

KillGooglePlayMusic()
LaunchGooglePlayMusic()
Activity()



