import re
import time
import os
import unittest,time
def check_wifi():
        os.system("adb shell dumpsys wifi > wifi.txt")
        with open("wifi.txt","r+") as fp:
            lines=fp.readline()
            Enabled = re.search('Wi-Fi is enabled',lines,re.I)
            if Enabled:
                return(True)
            else:
                return(False)
def enable_wifi():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 23")
def disable_wifi():
    print("disabling....")
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    time.sleep(5)
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 19")
    os.system("adb shell input keyevent 23")
result=check_wifi()
if result:
    print("wifi is enabled")
    disable_wifi()
else:
    print("wifi is disabled")
    enable_wifi()
            
            
