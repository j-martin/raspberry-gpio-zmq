import RPi.GPIO as GPIO
import time

timer = 0.02 # seconds
print timer
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

channel = 26

GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
# Set up the GPIO channels - one input and one output
# GPIO.setup(26, GPIO.IN)
while True:
	if GPIO.event_detected(channel):
	    print('Button pressed')

# Input from pin 11
# while 1:
# 	val = GPIO.input(26)
# 	if val == 1:
# 		print 'the light is on' , val
# 	else:
# 		print 'the light is off'
# 	time.sleep(.25)


