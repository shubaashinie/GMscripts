
import os
import time
Pass_cnt=0
Fail_cnt=0
def CheckAPMState():
    os.system( "adb shell dumpsys wifi > wifi_log.txt")
    fd=open("wifi_log.txt","r+")
    buf = fd.read()
    s1='mAirplaneModeOn true'
    if(s1 in buf):
        print("ON")
        return(True)
    else:
        print("OFF")
        return(False)
    
def Toggle_APM():
    os.system( "adb shell am start -a android.settings.AIRPLANE_MODE_SETTINGS")
    os.system( "adb shell input tap 986 1606")
    os.system( "adb shell input keyevent 66")

Toggle_APM()    
if(CheckAPMState()):
    Pass_cnt+=1
else:
    Fail_cnt+=1
print("Pass cnt=",Pass_cnt)
print("Fail cnt=",Fail_cnt)

        
  


