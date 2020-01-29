import RPi.GPIO as gpio
from time import sleep

# 0 is white, means no line
# 1 is black, means line

# When white move forward
# When right is black and left is white, its right turn
# When right is white and left is black, its left turn
# When right and left both are black, its an intersection, decision making


def setupIR():
    leftIR = 18
    rightIR = 22

    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(leftIR, gpio.IN)
    gpio.setup(rightIR, gpio.IN)


def moveForward():
    print("Moving forward")


def moveRight():
    print("Its a right turn")


def moveLeft():
    print("Its a left turn")


def intersection():
    print("its an intersection, make decision")


while True:
    if(gpio.input(rightIR) == 0 and gpio.input(leftIR) == 0):
        moveForward()
    elif(gpio.input(rightIR) == 1 and gpio.input(leftIR) == 0):
        moveRight()
    elif(gpio.input(rightIR) == 0 and gpio.input(leftIR) == 1):
        moveLeft()
    elif(gpio.input(rightIR) == 1 and gpio.input(leftIR) == 1):
        intersection()
    else:
        print("No clear choice")
