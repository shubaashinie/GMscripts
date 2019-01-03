import time
import unittest
import re
import os
pass_cnt=0
fail_cnt=0
i=0
def drag_screen():
	os.system("adb shell input touchscreen swipe 905 24 817 1077")
def torch_on():
        os.system("adb shell input tap 990 176")
        
def torch_off():
        os.system("adb shell input tap 990 176")
def validation():
        os.system("adb logcat -m 100000>t.txt")
        with open("t.txt","r+") as fp:
                print("======")
                lines=fp.read()
                Enabled = re.search('torch status is now AVAILABLE_OFF',lines,re.I)
                if Enabled:
                        return True
                else:
                        return False
drag_screen()        
while (i<1):
    time.sleep(2)
    torch_on()
    time.sleep(2)
    if(validation()):
            pass_cnt+=1
    else:
            fail_cnt+=1
    torch_off()
    i+=1
print("pass:",pass_cnt)
print("fail",fail_cnt)    
