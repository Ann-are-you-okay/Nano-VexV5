import os
import sys
import serial
import time
try:
	VEX_PORT ='/dev/ttyACM0'
	ser=serial.Serial(VEX_PORT,115200,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,timeout=2)
	ser.isOpen()
except:
	VEX_PORT ='/dev/ttyACM1'
	ser=serial.Serial(VEX_PORT,115200,timeout=2)
	ser.isOpen()
ser.flush()
print("OK")

#message = "{}\n".format("0,4:0,-4").encode("utf-8")

while ser.isOpen():
	try:
		ser.write("as\n".encode("utf-8"))
		readText = ser.readline()
		
		print(readText)

		print(ser.out_waiting, 'out')
		print(ser.in_waiting, 'in')

	#time.sleep(2) #in sec
	except:
		print("FAIL")
		ser.close()
