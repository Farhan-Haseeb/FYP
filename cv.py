import RPi.GPIO as gpio
import time
import keyboard

leftPower = 12
rightPower = 16

Motor1 = 7
Motor2 = 11
Motor3 = 13
Motor4 = 15

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(leftPower, gpio.OUT)
gpio.setup(rightPower, gpio.OUT)
gpio.setup(Motor1, gpio.OUT)
gpio.setup(Motor3, gpio.OUT)
gpio.setup(Motor4, gpio.OUT)
gpio.setup(Motor2, gpio.OUT)

ml = gpio.PWM(leftPower, 50)
mr = gpio.PWM(rightPower, 50)


def SetAngle(angle):
    duty = angle / 18 + 2
    gpio.output(rightPower, True)
    mr.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(rightPower, False)
    mr.ChangeDutyCycle(0)

def speed(x):
    mr.start(5)
    ml.start(5)
    ml.ChangeDutyCycle(x)
    mr.ChangeDutyCycle(x)

def leftForward():
    gpio.output(leftPower, True)
    gpio.output(Motor1, True)
    gpio.output(Motor2, False)


def rightForward():
    gpio.output(rightPower, True)
    gpio.output(Motor3, True)
    gpio.output(Motor4, False)


def leftReverse():
    gpio.output(leftPower, True)
    gpio.output(Motor1, False)
    gpio.output(Motor2, True)


def rightReverse():
    gpio.output(rightPower, True)
    gpio.output(Motor3, False)
    gpio.output(Motor4, True)


def forward():
    leftForward()
    rightForward()
    speed(15)


def reverse():
    leftReverse()
    rightReverse()
    speed(15)

def turnLeft():
    leftReverse()
    rightForward()
    speed(30)


def turnRight():
    rightReverse()
    leftForward()
    speed(30)


while True:
    if keyboard.is_pressed('w'):
        forward()
    if keyboard.is_pressed('s'):
        reverse()
    if keyboard.is_pressed('a'):
        turnLeft()
    if keyboard.is_pressed('d'):
        turnRight()
    if keyboard.is_pressed('q'):
        gpio.output(leftPower, False)
        gpio.output(rightPower, False)
        ml.stop()
        mr.stop()
        gpio.cleanup()
        break
