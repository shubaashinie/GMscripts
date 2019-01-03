
import os
import time
import sys
Iterations=sys.argv[1]
Pass_cnt=0
Fail_cnt=0
def CheckAPMState():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    fd=open("wifi_log.txt","r+")
    buf = fd.read()
    s1='mAirplaneModeOn true'
    if(s1 in buf):
        return(True)
    else:
        return(False)
    
def LAUNCH_APM():
    os.system( "adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")

def Toggle_APM():
    os.system("adb shell input tap 466 1521")
    time.sleep(5)
    
LAUNCH_APM()
for i in range(int(Iterations)):
    if(CheckAPMState()):
        print("APM already enabled...disabling APM")
        Toggle_APM()
    print("APM disabled and enabling APM")
    Toggle_APM()
    time.sleep(5)    
    if(CheckAPMState()):
        print("APM enabled")
        Pass_cnt+=1
    else:
        print("APM disabled")
        Fail_cnt+=1
time.sleep(5)
if(CheckAPMState()):
    Toggle_APM()
print("Pass cnt=",Pass_cnt)
print("Fail cnt=",Fail_cnt)

        



