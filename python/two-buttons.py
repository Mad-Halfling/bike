#  Two Buttons- using python rev 3 
#  Writen by Ray Eacott 

import RPi.GPIO as GPIO    # import GPIO control modual

GPIO.setmode(GPIO.BOARD)   # set RPi to use pin numbers
GPIO.setwarnings(False)    # switch off error messages
GPIO.setup(21, GPIO.OUT)   # setup pin 21 as output
GPIO.setup(8, GPIO.IN)     # setup pin 8 as input
GPIO.setup(10, GPIO.IN)    # setup pin 10 as input

while True:
	
	Button1 = GPIO.input(8)         #  test to see if button 1 pressed
	if Button1 == False:            # if pressed switch on buzzer
		GPIO.output(21, True)       # switch on Buzzer
	else: 
		Button2 = GPIO.input(10)    # test button 2
		if Button2 == False:        # if pressed switch off buzzer
			GPIO.output(21, False)  # switch off Buzzer
		next
			
	




