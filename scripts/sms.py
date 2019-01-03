import os
import time
import re
import unittest,time
def kill_sms():
    os.system("adb shell am force-stop com.android.mms")
def launch_sms():
    os.system("adb shell am start -a android.intent.action.SENDTO -d sms:918985259304 --es sms_body hiii --ez exit_on_sent true")
    time.sleep(2)
    os.system("adb shell input tap 663 743")
    os.system("adb shell input keyevent 22")
    os.system("adb shell input keyevent 66")
kill_sms()
launch_sms()
