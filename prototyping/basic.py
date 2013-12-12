import RPi.GPIO as GPIO
import time

# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO channels - one input and one output
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


# Input from pin 11
# input_value = GPIO.input(11)

# Output to pin 12
while True:


	GPIO.output(12, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(11, GPIO.LOW)

	time.sleep(0.5)

	GPIO.output(26, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(12, GPIO.LOW)
	time.sleep(0.5)

	GPIO.output(26, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(11, GPIO.HIGH)

	time.sleep(0.5)

# The same script as above but using BCM GPIO 00..nn numbers
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)
#GPIO.setup(18, GPIO.OUT)
##input_value = GPIO.input(17)
#GPIO.output(18, GPIO.HIGH)
