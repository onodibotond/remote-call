import os
import sys
from conf import *
from win32 import win32gui
import win32con, win32console

if RESIZE_WINDOW:
	print("HERE")
	os.system("mode con cols=" + COLUMN_NUMBER)
	os.system("mode con lines=" + LINESS_NUMBER)

if KEEP_IN_FRONT:
	print("HERE")
	hWnd=int(win32console.GetConsoleWindow())
	win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

adb = ADB_PATH
device = DEVICE_ID

if device == '':
	try:
		stream = os.popen(adb + " devices")
		out = stream.read()
		device = out.split('\n')[1].split('\t')[0]
	except:
		print("ERROR: No device connected")
		print("Try running in a cmd window: adb.exe devices")

if device == '':
	#logging to be done
	exit()

while (True):
	#os.system('cls')
	number = input(TEXT + ": ")
	number = number.replace(" ","")

	if number:
		print("Calling: " + number)
		#LOG: print(adb + "-s \"" + device + "\" shell am start -a android.intent.action.CALL -d tel:\"" + number + "\"")
		stream = os.popen(adb + " -s \"" + device + "\" shell am start -a android.intent.action.CALL -d tel:\"" + number + "\"")
