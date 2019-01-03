import os
import time

pass_cnt=0
fail_cnt=0
iterations=4
def scrsht():
	os.system("adb shell screencap -p /sdcard/screencap.png")
	os.system("adb pull /sdcard/screencap.png")
def test(): 
    os.system("adb logcat -d >scrn.txt")
    with open("scrn.txt","r+") as fh:
            #string="com.android.systemui/.screenshot.TakeScreenshotService"
            string="Internal Memory    -    /storage/emulated/0/Pictures/Screenshots"
            cnt=0
            while 1:
                    lines= fh.readline()
                    if (string in lines):
                            cnt+=1
                    if (lines==""):
                            break
            print(cnt)
            return cnt

for i in range(int(iterations)):
        scrsht()
        if(test()==int(iterations)+1):
                pass_cnt+=1
        else:
                fail_cnt+=1
print("pass_cnt:",pass_cnt)
print("fail_cnt:",fail_cnt)


 
