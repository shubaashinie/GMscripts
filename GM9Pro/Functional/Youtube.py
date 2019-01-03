import os
from time import sleep
def LaunchYoutube():
    os.system("adb shell monkey -p com.google.android.youtube -c android.intent.category.LAUNCHER 1")
    sleep(5)
    os.system("adb shell input keyevent 84")
    os.system("adb shell input text Songs")
    for i in range(0,2):
        os.system("adb shell input keyevent 66")
        sleep(2)
    
def KillYoutube():
    os.system("adb shell am force-stop com.google.android.youtube")

KillYoutube()
LaunchYoutube()

