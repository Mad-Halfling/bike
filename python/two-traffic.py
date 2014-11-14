# TWO way traffic lights  Written by Ray Eacott

#  Version 2.0   date 13/10/2014

#  This for Python ver 3.2

import RPi.GPIO as GPIO     # import Python GPIO modual
import time                 # import time modual
GPIO.setmode(GPIO.BOARD)    # use board numbers
GPIO.setwarnings(False)

Red1 = 12          # Assign GPIO pins numbers to Lights    
Orange1 = 16
Green1 = 18
Red2 = 11
Orange2 = 13
Green2 = 15

# Delay times in seconds

Orange = 1  
Traffic = 5  # Traffic flowing through road works
Clear = 2   

# Setup GPIO 

GPIO.setup(Red1, GPIO.OUT)     # set pin Red1 to output
GPIO.setup(Orange1, GPIO.OUT)  # set Orange1 to output
GPIO.setup(Green1, GPIO.OUT)   # set Green1 to output

GPIO.setup(Red2, GPIO.OUT)     # set Red2 to output
GPIO.setup(Orange2, GPIO.OUT)  # set Orange22 to output
GPIO.setup(Green2, GPIO.OUT)   # set Green2 to output

# Switch on both Red lights all other lights off

GPIO.output(Red1, True)        # switch on Red1        
GPIO.output(Orange1, False)    # switch off Orange1
GPIO.output(Green1, False)     # switch off Green1
GPIO.output(Red2, True)        # switch on Red2
GPIO.output(Orange2, False)    # switch off Orange2
GPIO.output(Green2, False)     # switch off Green2

time.sleep(Clear)  	 # to allow traffic to clear from the road works  

for lights in range(1,10):       # Repeat 10 times
    
	GPIO.output(Orange1, True)   # Orange on 
	time.sleep(Orange)           # small delay
	GPIO.output(Red1, False)     # Red off
	GPIO.output(Orange1, False)  # Orange off
	GPIO.output(Green1, True)    # Green on
	
	time.sleep(Traffic)
	
	GPIO.output(Green1, False)
	GPIO.output(Orange1, True)
	time.sleep(Orange)
	GPIO.output(Orange1, False)
	GPIO.output(Red1, True)
	time.sleep(Clear)   # to allow traffic to clear from the road works
		
	GPIO.output(Orange2, True)
	time.sleep(Orange)
	GPIO.output(Red2, False)
	GPIO.output(Orange2, False)
	GPIO.output(Green2, True)
	
	time.sleep(Traffic)
	
	GPIO.output(Green2, False)
	GPIO.output(Orange2, True)
	time.sleep(Orange)
	GPIO.output(Orange2, False)
	GPIO.output(Red2, True)
	time.sleep(Clear)   # to allow traffic to clear from the road works 
	
	next
	
GPIO.cleanup()








