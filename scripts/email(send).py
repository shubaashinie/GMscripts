import os
import time
#fields=['testcase','passcnt','failcnt']
iterations=1
pass_cnt=0
fail_cnt=0
def kill_mail():
        os.system("adb shell am force-stop com.google.android.gm")
def launch_mail():
        os.system("adb shell am start -n com.google.android.gm/com.google.android.gm.ConversationListActivityGmail")
        time.sleep(1)
        os.system("adb shell input tap 973 1880")
        time.sleep(1)
def compose_mail():
    os.system("adb shell input text innomindsgm@gmail.com")
    for i in range(1,3):
            os.system("adb shell input keyevent 66") 
    os.system("adb shell input text hii")
    for i in range(1,3):
            os.system("adb shell input keyevent 19") 
    os.system("adb shell input text test")
def attach_mail():
        os.system("adb shell input tap 787 156")
        for i in range(1,3):
                os.system("adb shell input keyevent 20")     #for attachements in the mail
                os.system("adb shell input keyevent 66")
                time.sleep(1)
        os.system("adb shell input tap 908 155")
def test():
    os.system("adb logcat -d >gmail.txt")
    with open("gmail.txt","r+") as fh:
            cnt=0
            string="activation: Account innomindsgm@gmail.com"
            while 1:
                    lines= fh.readline()
                    print(lines)
                    if (string in lines):
                        cnt+=1
                    if (lines==""):
                        break
            print(cnt)
            return(cnt)
kill_mail()         
for i in range(int(iterations)):
        launch_mail()
        compose_mail()
        attach_mail()
        time.sleep(5)
        if(test()==int(iterations)+1):
                pass_cnt+=1
        else:
                fail_cnt+=1
        kill_mail()
print("pass_cnt:",pass_cnt)
print("fail_cnt:",fail_cnt)

