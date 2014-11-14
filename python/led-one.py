#  Flash one LED - using python rev 3 
#  Writen by Ray Eacott 

import RPi.GPIO as GPIO  # import 
import time

GPIO.setmode(GPIO.BOARD)   # set RPi to use pin numbers
GPIO.setwarnings(False)    # switch off error messages
GPIO.setup(12, GPIO.OUT)   # setup pin 12 as output

for loop in range(1, 10):  # repeat 10 times

		GPIO.output(12, True)  # switch on LED
		time.sleep(1)          # wait 1 second
		GPIO.output(12, False) # switch off LED
		time.sleep(1)          # wait 1 second

next

GPIO.cleanup()                 # reset GPIO program

