import os
import sys
from conf import *

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

number = sys.argv[1]
number = number.replace(" ","")

if number:
	print("Calling: " + number)
	stream = os.popen(adb + " -s \"" + device + "\" shell am start -a android.intent.action.CALL -d tel:\"" + number + "\"")
