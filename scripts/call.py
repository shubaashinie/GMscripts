#import os
#import sys
#import time
#os.system("adb shell input tap 90 1187")
#os.system( "adb shell input keyevent 5")
#
#os.system( "adb shell input text 6300347124")
#os.system("adb shell input tap 363 1108")
#os.system( "adb shell input keyevent 5")
#)
#////////////make call///////////
#os.system("adb shell am start -a android.intent.action.INSERT -t vnd.android.cursor.dir/contact -e name 'Yoga@innominds' -e phone 9159495244")
#os.system("adb shell am start -a android.intent.action.CALL -d tel:9159495244")
#time.sleep(15) 
#os.system( "adb shell input keyevent 6")# /// end call after 15 sec
#//////////////send message ////////////////
#os.system("adb shell am start -a android.intent.action.SENDTO -d sms:+919159495244 --es sms_body 'hi dis is yoga' --ez exit_on_sent true")
#os.system("adb shell input keyevent 22")
#os.system("adb shell input keyevent 66")
#os.system("adb shell input keyevent 3")
#/////////////
"""os.system("adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
os.system("adb shell am start -a android.settings.BLUETOOTH_SETTINGS")
os.system("adb shell service call bluetooth_manager 6")
os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings")"""
#////////
#os.system("adb shell svc wifi enable")
#os.system("adb shell svc wifi disable")

#/////////pull contact to desktop
#os.system("adb pull /data/data/com.android.providers.contacts/databases/contacts2.db /Desktop")


#//////////////////////Bluetooth enable disable
#import os
#import sys
#import time
#import re
#import unittest,time

"""
print("=======================================================================")
print("Bluetooth enable disable test started")
print("=======================================================================")
from sys import argv
Iterations = 3#argv[1] 

pass_TC_count = 0
fail_TC_count = 0
print("Iterations:",Iterations)
def Checkbtstate():
    os.system( "adb shell dumpsys bluetooth_manager > bt_log.txt")
    bt_log = open("bt_log.txt","r+")
    buffer = bt_log.readline();
    bt_log.close()
    Enabled = re.search('enabled: true', buffer, re.I)
    if Enabled:
        return(True)
    else:
        return(False)

def CheckbtConnectedstate():
    os.system("adb shell input tap 265 430")
    time.sleep(5)
    os.system( "adb shell dumpsys bluetooth_manager > bt_log.txt")
    with open("bt_log.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            string1="  mPhoneState: com.android.bluetooth.hfp.HeadsetPhoneState@3dcd6230"
            if(string1 in line):
                #print("connected")
                return(True)

def Toggle_bt():
    os.system("adb shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings")
    os.system("adb shell input tap 662 207")
    #os.system("adb shell input  23")
    #time.sleep(5)
#Turn OFF wifi before starting testcases
#checking for wifi state
state = Checkbtstate()
print(state)
if state:
    Toggle_bt()
    
for n in range(int(Iterations)):
    Toggle_bt()
    time.sleep(5)
    Connectedstate = CheckbtConnectedstate()
    if Connectedstate:
        print("Connected to paired device successfully for iteration:", n)
        pass_TC_count = pass_TC_count+1
    else:
        print("Not connected to paired device  for iteration:", n)
        fail_TC_count = fail_TC_count+1
    Toggle_bt()
print("Bluetooth preset connection Passed:",pass_TC_count )
print("Bluetooth preset connection Failed:",fail_TC_count )"""


#///////////////////// playing mp3 and mp4
"""import os
import sys
import time
import re
import unittest,time

from sys import argv
Iterations = 1 #argv[1] 

def Killmusic():
    os.system( "adb shell am force-stop com.google.android.music")

def Launchmusic():
    os.system( "adb shell am start -a android.intent.action.VIEW -d file:///internal storage/ucdownloads/[isong.info]03-Prema Prema.mp3 -t audio/mp3")
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
#/////////////////// mo call

import os
import time
import sys
count=1 #int(sys.argv[1])
n=1
pass_TC = 0
fail_TC = 0
def mo_call_test():
    os.system("adb shell getprop >gsm.txt ")
    with open("gsm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
            string1="[gsm.sim.state]: [READY,READY]"
            string2 = "[gsm.sim.state]: [READY,NOT_READY]"
            string3 = "[gsm.sim.state]: [NOT_READY,READY]"
            string4 = "[gsm.sim.state]: [ABSENT,READY]"
            string5 = "[gsm.sim.state]: [READY,ABSENT]"
            if (string1 in line or string2 in line or string3 in line or string4 in line or string5 in line):
                print("Sim present, so procedding the test")
                break
        else:
            print("sim not present, please insert the sim and start the test")
    os.system("adb wait-for-device shell input keyevent 82")
    os.system("adb wait-for-device shell input keyevent 3")
    os.system( "adb shell dumpsys telephony.registry > mCallState.txt")
    time.sleep(5)
    with open("mCallState.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            #print(line)
            string1="mCallState=2"
            if(string1 in line):
                print("Call already connected and in progress...\n")
                print("Ending the call \n")
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                break
    print("Connecting the call to MT_num...\n")
    os.system("adb shell am start -a android.intent.action.CALL -d tel:9159495244")
    time.sleep(10)
    os.system("adb shell dumpsys telephony.registry > mCallState1.txt")
    time.sleep(5)
    with open("mCallState1.txt", "r+") as fh:
        lines = fh.readlines()
        for line in lines:
            # print(line)
            #print("checking for call status")
            string2 = "mCallState=2"
            if (string2 in line):
                print("Call successfully connected and in progress...\n")
                print("Ending the call \n")
                time.sleep(5)
                os.system("adb shell input keyevent KEYCODE_ENDCALL")
                print("Call successfully disconnected ...\n")
                test=1
                #break
                return 1
        else:
            print("Unable to connect the call, so test case is failed")
            return 0



while(count!=0):
    print("Itr", n )
    print("--------------------------------")
    n=n+1
    x=mo_call_test()
    if(x==1):
        pass_TC += 1
        print("Test case = PASS ...\n")
        print("--------------------------------")
    else:
        fail_TC += 1
        ("Test case = FAIL ...\n")
        print("--------------------------------")
    count=count-1
print ("--------------------------------")
print ("Total NO.OF Iterations ran : " , n-1)
print ("Total NO.OF iterations Passed: %d" %pass_TC)
print ("Total NO.OF iterations Failed: %d" %fail_TC)
print ("---------------------------------")



