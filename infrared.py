import RPi.GPIO as GPIO
from time import sleep

class IR():
	def __init__(self):
		self.rightSensor = 18
		self.leftSensor = 22
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.rightSensor,GPIO.IN)
		GPIO.setup(self.leftSensor,GPIO.IN)
		self.L_in = GPIO.input(self.leftSensor)
		self.R_in = GPIO.input(self.rightSensor)
		self.lib = GPIO

