import RPi.GPIO as GPIO
import time

timer = 0.02 # seconds
print timer
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

# Set up the GPIO channels - one input and one output
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


# Input from pin 11
# input_value = GPIO.input(11)

# Output to pin 12
while True:
	for x in [26,24,23,21,19]:

		GPIO.output(x, GPIO.HIGH)
		time.sleep(timer)
		GPIO.output(x, GPIO.LOW)

