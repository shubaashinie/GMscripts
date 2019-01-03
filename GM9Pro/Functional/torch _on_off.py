import time
import unittest
import os

i=0
def drag_screen():
	os.system("adb shell input touchscreen swipe 905 24 817 1077")
def torch_on():
        os.system("adb shell input tap 990 176")
        
def torch_off():
        os.system("adb shell input tap 990 176")

drag_screen()        
while (i<10):
    time.sleep(2)
    torch_on()
    time.sleep(2)
    torch_off()
    i+=1
    
