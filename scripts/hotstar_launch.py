import os
import time
pass_cnt=0
fail_cnt=0
iterations=3

def launch_hotstar():
    os.system("adb shell monkey -p in.startv.hotstar 1")
    time.sleep(10)

def act():
    os.system("adb shell input tap 160 1242")
    time.sleep(5)
    
def kill_hotstar():
    os.system("adb shell am force-stop in.startv.hotstar")
    
def validate():
    os.system("adb shell dumpsys activity >hot.txt")
    s="launchedFromPackage=in.startv.hotstar"
    with open("hot.txt","r+") as fh:
        buf=fh.read() 
        if s in buf:
            return 1
        else:
            return 0

def switch_mobiledata():
    os.system("adb shell svc data enable")
    time.sleep(3)

def checkmobiledata():
    os.system("adb shell getprop>mobiledata.txt")
    fp=open("mobiledata.txt","r+")
    buff=fp.read()
    str1="[gsm.defaultpdpcontext.active]: [true]"
    if str1 in buff:
        print(str1)
        return 1
    else:
        return 0

kill_hotstar()
switch_mobiledata()
for i in range(int(iterations)):
    if(checkmobiledata()):
        launch_hotstar()
        act()
        if(validate()):
            pass_cnt+=1
        else:
            fail_cnt+=1
        kill_hotstar()
    else:
        print("mobile data is off.....can't proceed the test")

print("pass_cnt:",pass_cnt)
print("fail_cnt:",fail_cnt)
