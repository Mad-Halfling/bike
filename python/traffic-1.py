# Traffic Lights  25/10/2014

# Writen by Ray Eacott  Rev 2 for use with python 3.2 


import RPi.GPIO as GPIO    # import GPIO library
import time                # import time modual so we can use the sleep funtion

GPIO.setmode(GPIO.BOARD)   #  Use pin numbers
GPIO.setwarnings(False)

Red = 12                   #  Pin for Red LED etc
Orange = 16
Green = 18

GPIO.setup(Red, GPIO.OUT)   # set pin 12 to output
GPIO.setup(Orange, GPIO.OUT)   # set pin 16 to output
GPIO.setup(Green, GPIO.OUT)   # set pin 18 to output

for traffic in range(1,10):


	GPIO.output(Red, True)        # switch on Red LED
	time.sleep(2)                 # wait 2 sec
	GPIO.output(Orange, True)     # switch on Orange LED
	time.sleep(2)                 # wait 2 sec
	              
	GPIO.output(Red, False)       # switch off Red LED
	GPIO.output(Orange, False)    # switch off Orange LED
	GPIO.output(Green, True)      # switch on Green LED     
	time.sleep(2)                 # wait 2 sec
	GPIO.output(Green, False)     # switch off Green LED
	
	GPIO.output(Orange, True)     # switch on Orange LED    
	time.sleep(2)                 # wait 2 sec
	GPIO.output(Orange, False)    # switch off Orange LED            
	
	next                          # start again	
	
GPIO.cleanup()                      # reset GPIO pins
