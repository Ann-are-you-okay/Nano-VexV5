import serial

with serial.Serial('/dev/ttyACM0', 115200, timeout=10) as ser:
	while True:
		print(ser.readline())
