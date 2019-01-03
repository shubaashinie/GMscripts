import os
import time
import re
import unittest,time
def kill_camera():
	os.system("adb shell am force-stop com.android.camera2")
def launch_camera():
	os.system("adb shell am start -a android.media.action.IMAGE_CAPTURE")
def capture_start_stop():
	os.system("adb shell input keyevent KEYCODE_CAMERA")
def launch_video():
	os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE")

kill_camera()
launch_camera()
print("camera launching.............")
time.sleep(5)
capture_start_stop()
print("camera captured.............")
os.system("adb shell input tap 641 1200")
launch_video()
capture_start_stop()
print("video capturing.............")
capture_start_stop()
time.sleep(10)
capture_start_stop()

