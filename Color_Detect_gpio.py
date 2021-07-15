import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

output_pin = 18 #pin BCM18 is pin 12 on the board

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
YELLOW = (0, 255, 255)

#FOR VIDEO 
dispW = 640
dispH = 480
flip = 2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap = cv2.VideoCapture(camSet) #0 for webcam

def empty(a):
	pass

GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH) #set pin 12 to output

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)

area1 = (480,120)
area2 = (160,120)
print("Starting/n")
curr_value = GPIO.HIGH #initialize curr_value to HIGH

while True:
	success,img = cap.read() #get frame
	imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #change image into hsv colorspace

	h_min = cv2.getTrackbarPos("HUE Min","HSV")
	h_max = cv2.getTrackbarPos("HUE Max","HSV")
	s_min = cv2.getTrackbarPos("SAT Min","HSV")
	s_max = cv2.getTrackbarPos("SAT Max","HSV")
	v_min = cv2.getTrackbarPos("VALUE Min","HSV")
	v_max = cv2.getTrackbarPos("VALUE Max","HSV")

	lower = np.array([h_min,s_min,v_min])
	upper = np.array([h_max,s_max,v_max])
	mask = cv2.inRange(imgHsv,lower,upper)
	result = cv2.bitwise_and(img,img,mask = mask)

	x = int(dispW/2)
	y = int(dispH/2)

	cv2.line(result,(x,dispW),(x,0),YELLOW,2)

	cv2.circle(result,area1,3,(0,0,255),3)
	cv2.circle(result,area2,3,(0,0,255),3)


	cv2.imshow("Mask",mask)
	cv2.imshow("Result",result)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break	
	
	#if dected color is on RIGHT side => HIGH on pin 12
	if (mask[area1[1]][area1[0]] == 255):
		print("RIGHT")
		curr_value = GPIO.HIGH
		GPIO.output(output_pin, curr_value)
	#if detected color is on LEFT side => LOW on pin 12
	elif (mask[area2[1]][area2[0]] == 255):
		print("LEFT")
		curr_value = GPIO.LOW
		GPIO.output(output_pin, curr_value)
	else:
		print("STAY")
		
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()
