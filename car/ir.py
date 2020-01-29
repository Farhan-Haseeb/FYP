import RPi.GPIO as gpio

# 0 is white, means no line
# 1 is black, means line

# When white move forward
# When right is black and left is white, its right turn
# When right is white and left is black, its left turn
# When right and left both are black, its an intersection, decision making

leftIR = 18
rightIR = 22

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(leftIR, gpio.IN)
gpio.setup(rightIR, gpio.IN)


def detectWay():
    if(gpio.input(rightIR) == 0 and gpio.input(leftIR) == 0):
        return "Forward"
    elif(gpio.input(rightIR) == 1 and gpio.input(leftIR) == 0):
        return "Right"
    elif(gpio.input(rightIR) == 0 and gpio.input(leftIR) == 1):
        return "Left"
    elif(gpio.input(rightIR) == 1 and gpio.input(leftIR) == 1):
        return "Intersection"
