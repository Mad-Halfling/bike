#  Buzzer - using python rev 3 
#  Writen by Ray Eacott 

import RPi.GPIO as GPIO  # import 
import time

GPIO.setmode(GPIO.BOARD)   # set RPi to use pin numbers
GPIO.setwarnings(False)    # switch off error messages
GPIO.setup(21, GPIO.OUT)   # setup pin 21 as output
GPIO.setup(8, GPIO.IN)

while True:
	test = GPIO.input(8)
	if test == True: 
		GPIO.output(21, False)
	else: 
		GPIO.output(21, True)
		next	




