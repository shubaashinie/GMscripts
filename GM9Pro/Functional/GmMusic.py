import os
from time import sleep

def KillGmMusic():
    os.system("adb shell am force-stop com.generalmobile.app.musicplayer")
def LaunchGmMusic():
    os.system("adb shell monkey -p com.generalmobile.app.musicplayer -c android.intent.category.LAUNCHER  1")
    sleep(2)
def Activity():
    os.system("adb shell input tap 536 1290")
    for i in range(0,2):
        sleep(3)
        os.system("adb shell input keyevent 85")
KillGmMusic()
LaunchGmMusic()
Activity()
