import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.output(12, True)


while True:
	gpio.output(7, True)
	gpio.output(11, False)
