import RPi.GPIO as GPIO
import time

timer = 0.02 # seconds
print timer
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO channels - one input and one output
the_list = []
for x in xrange(0,28):
	print x
	try:
		GPIO.setup(x, GPIO.IN)
		print 'ok'
		the_list.append(x)
	except:
		print 'failed'

print the_list

# Input from pin 11
while 1:
	val = GPIO.input(26)
	if val == 1:
		print 'the light is on' , val
	else:
		print 'the light is off'
	time.sleep(.25)


