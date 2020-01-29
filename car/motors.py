import RPi.GPIO as gpio
import keyboard
import time

leftPower = 12
rightPower = 16

Motor1 = 7
Motor2 = 11
Motor3 = 13
Motor4 = 15

acceleration = 15
turnSpeed = 35

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


def SetAngle(rightAngle, leftAngle):
    mr.start(0)
    ml.start(0)

    Rightduty = rightAngle / 18 + 2
    Leftduty = leftAngle / 18 + 2

    rightReverse()
    leftForward()

    print(Rightduty)
    print(Leftduty)

    gpio.output(rightPower, True)
    gpio.output(leftPower, True)
    # mr.ChangeDutyCycle(Rightduty)
    # ml.ChangeDutyCycle(Leftduty)
    mr.ChangeDutyCycle(7.5)
    ml.ChangeDutyCycle(18.5)
    time.sleep(1)
    gpio.output(rightPower, False)
    gpio.output(leftPower, False)
    mr.ChangeDutyCycle(0)
    ml.ChangeDutyCycle(0)


    mr.stop()
    ml.stop()


def speed(x):
    mr.start(0)
    ml.start(0)
    ml.ChangeDutyCycle(x)
    mr.ChangeDutyCycle(x)


def leftForward():
    gpio.output(rightPower, True)
    gpio.output(Motor1, True)
    gpio.output(Motor2, False)


def rightForward():
    gpio.output(leftPower, True)
    gpio.output(Motor3, True)
    gpio.output(Motor4, False)


def leftReverse():
    gpio.output(rightPower, True)
    gpio.output(Motor1, False)
    gpio.output(Motor2, True)


def rightReverse():
    gpio.output(leftPower, True)
    gpio.output(Motor3, False)
    gpio.output(Motor4, True)


def forward():
    leftForward()
    rightForward()
    speed(acceleration)


def reverse():
    leftReverse()
    rightReverse()
    speed(acceleration)


def turnLeft():
    leftReverse()
    rightForward()
    speed(turnSpeed)


def turnRight():
    rightReverse()
    leftForward()
    speed(turnSpeed)
    # SetAngle(90, 270)


def stop():
    gpio.output(Motor1, False)
    gpio.output(Motor2, False)
    gpio.output(Motor3, False)
    gpio.output(Motor4, False)
    gpio.output(leftPower, False)
    gpio.output(rightPower, False)
    # gpio.cleanup()
# import RPi.GPIO as gpio
# import keyboard

# leftPower = 12
# rightPower = 16

# Motor1 = 7
# Motor2 = 11
# Motor3 = 13
# Motor4 = 15

# acceleration = 15
# turnSpeed = 35

# gpio.setwarnings(False)
# gpio.setmode(gpio.BOARD)
# gpio.setup(leftPower, gpio.OUT)
# gpio.setup(rightPower, gpio.OUT)
# gpio.setup(Motor1, gpio.OUT)
# gpio.setup(Motor3, gpio.OUT)
# gpio.setup(Motor4, gpio.OUT)
# gpio.setup(Motor2, gpio.OUT)

# ml = gpio.PWM(leftPower, 50)
# mr = gpio.PWM(rightPower, 50)

# def SetAngle(angle):
#     duty = angle / 18 + 2
#     gpio.output(rightPower, True)
#     mr.ChangeDutyCycle(duty)
#     sleep(1)
#     GPIO.output(rightPower, False)
#     mr.ChangeDutyCycle(0)

# def speed(x):
#     mr.start(0)
#     ml.start(0)
#     ml.ChangeDutyCycle(x)
#     mr.ChangeDutyCycle(x)


# def leftForward():
#     gpio.output(rightPower, True)
#     gpio.output(Motor1, True)
#     gpio.output(Motor2, False)


# def rightForward():
#     gpio.output(leftPower, True)
#     gpio.output(Motor3, True)
#     gpio.output(Motor4, False)


# def leftReverse():
#     gpio.output(rightPower, True)
#     gpio.output(Motor1, False)
#     gpio.output(Motor2, True)


# def rightReverse():
#     gpio.output(leftPower, True)
#     gpio.output(Motor3, False)
#     gpio.output(Motor4, True)


# def forward():
#     leftForward()
#     rightForward()
#     speed(acceleration)


# def reverse():
#     leftReverse()
#     rightReverse()
#     speed(acceleration)


# def turnLeft():
#     leftReverse()
#     rightForward()
#     speed(turnSpeed)


# def turnRight():
#     rightReverse()
#     leftForward()
#     speed(turnSpeed)


# def stop():
#     gpio.output(Motor1, False)
#     gpio.output(Motor2, False)
#     gpio.output(Motor3, False)
#     gpio.output(Motor4, False)
#     gpio.output(leftPower, False)
#     gpio.output(rightPower, False)
#     # gpio.cleanup()
