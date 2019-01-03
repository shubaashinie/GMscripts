import datetime
from Creat_alarm import alarm,func
from time import strftime,sleep
import os
import sys
LaunchPassCnt=0
LaunchFailCnt=0
Ring_pass_cnt=0
Ring_fail_cnt=0
iterations=1#sys.argv[1]

print("---------------Alarm-----------------")

def kill_alarm():
    os.system("adb shell am force-stop com.google.android.deskclock")

def validate():
    os.system( "adb shell dumpsys activity > alarm.txt")
    with open("alarm.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1="packageName=com.google.android.deskclock processName=com.google.android.deskclock"
            if(s1 in line):
                return(True)
        return(False)

def Checkalarmstate(timee,data):
    os.system( "adb shell dumpsys alarm > aaaa.txt")
    with open("aaaa.txt","r+") as fh:
        lines=fh.readlines()
        for line in lines:
            s1=timee
            s2="user:0 pendingSend:false time:"
            if((s1 in line) or (s2 in line)):
                return(True)
        return(False)

def Launch_alarm():
    os.system("adb shell am start -n com.google.android.deskclock/com.android.deskclock.DeskClock")

for i in range(int(iterations)):
    kill_alarm()
    Launch_alarm()
    if(validate()):
        LaunchPassCnt+=1
    else:
        LaunchFailCnt+=1
    timee=datetime.datetime.now().strftime('%H:%M:%S')
    reg=timee.split(':')
    a=reg[1]
    hr=reg[0]
    minu=(int(a)+1 )
    alarm(hr,minu)
    data=str(hr)+':'+str(minu)
    print(data)
    print("Alarm is ON")
    while(Checkalarmstate(timee,data)):
        pass
    if(Checkalarmstate(timee,data)):
        Ring_fail_cnt+=1
    else:
        Ring_pass_cnt+=1
        print("Alarm is ringing")
        os.system("adb shell input keyevent 3")
        os.system("adb shell input tap 804 375")
        kill_alarm()
print("Launch Pass count:",LaunchPassCnt,",Fail Count:",LaunchFailCnt)
print("Alarm Ringing pass_cnt,Alarm Ringing fail_cnt:",Ring_pass_cnt,Ring_fail_cnt)
