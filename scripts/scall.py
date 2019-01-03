import os
import time
import re
import unittest,time
os.system("adb shell am start -a android.intent.action.CALL -d tel:918985259304")
print("calling")
os.system("adb shell input keyevent 20")#selecting sim card
os.system("adb shell input keyevent 66")#enter
time.sleep(2)
os.system("adb shell input keyevent 6") #hanging up
