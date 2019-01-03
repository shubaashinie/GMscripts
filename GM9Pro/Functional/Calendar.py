import os
from time import sleep
def launch_Calendar():
    os.system("adb shell monkey -p com.google.android.calendar -c android.intent.category.LAUNCHER 1")
def kill_Calendar():
        os.system("adb shell am force-stop com.google.android.calendar")
kill_Calendar()
sleep(4)
launch_Calendar()
os.system("adb shell input tap 935 1878")
os.system("adb shell input tap 951 1890")
os.system("adb shell input text TestingEvent")
os.system("adb shell input tap 987 1963")
os.system("adb shell input tap 1010 161")
