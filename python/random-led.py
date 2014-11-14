# Random flashing LED - works in Python 3.2

# Same kit as Road Works Traffic lights

# Writen by Ray Eacott  23/10/2014

import RPi.GPIO as GPIO    # import GPIO library
import random
import time

GPIO.setmode(GPIO.BOARD)   # use pin numbers
GPIO.setwarnings(False)    # switch off error messages

one = 12    # GPIO pin for first LED etc
two = 16
three = 18
four = 11
five = 13
six = 15

GPIO.setup(one, GPIO.OUT)   # set pins to output
GPIO.setup(two, GPIO.OUT)
GPIO.setup(three, GPIO.OUT)
GPIO.setup(four, GPIO.OUT)
GPIO.setup(five, GPIO.OUT)   
GPIO.setup(six, GPIO.OUT)   
   
for n in range(1, 10):
	
	GPIO.output(one, False)     # switch off all LEDs
	GPIO.output(two, False)
	GPIO.output(three, False)
	GPIO.output(four, False)
	GPIO.output(five, False)
	GPIO.output(six, False)

	num = random.randint(1,6)   # get a random number between 1 and 6
		
	if num == 1:
		GPIO.output(one, True)  # switch on LED 1      
		 				
	elif num == 2: 
		GPIO.output(two, True)  # switch on LED 2  etc.
			
	elif num == 3: 
		GPIO.output(three, True) 
			
	elif num == 4: 
		GPIO.output(four, True) 
				
	elif num == 5:
		GPIO.output(five, True) 
			
	elif num == 6:
		GPIO.output(six, True)
					
	time.sleep(1)    # wait for 1 second to allow display to be seen			
					
	next
	
GPIO.cleanup() 
				
		
		
	
		
		 
	
	              
	
	
	
	
