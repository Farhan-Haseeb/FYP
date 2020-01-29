from ir import detectWay
from motors import forward, reverse, turnLeft, turnRight, stop
# from rfid import rfid
from sonar import Sonar
import time

run = False

turningTime = time.time() + 60 * 0.01
# turningTime = time.time() + 60 * 0.01

t_end = time.time() + 60 * 0.1

isForward = False
isRight = False
isLeft = False
isIntersection = False


def turnCycle():
    print("assad")
    # stop()
    # time.sleep(2)
    # forward()
    # time.sleep(0.5)
    stop()
    time.sleep(1)
    turnRight()
    time.sleep(0.33)
    stop()
    # while time.time() < turningTime:
    #     if isRight != True:
    #         print("ssssss")
    #     print("23234324")
    #     if isRight != True:
    #         turnRight()
    #         isRight = True


turnTiming = 0.41

while True:
    if isForward != True:
        forward()
        # while True:
        #     if Sonar():
        #         break
        time.sleep(2)
        turnCycle()
        forward()
        time.sleep(2)
        stop()
        time.sleep(1)
        turnLeft()
        time.sleep(turnTiming)
        stop()
        time.sleep(1)
        forward()
        time.sleep(2)
        stop()
        time.sleep(1)
        turnLeft()
        time.sleep(turnTiming)
        stop()
        time.sleep(1)

        forward()
        time.sleep(2)
        stop()
        time.sleep(1)
        turnLeft()
        time.sleep(turnTiming)
        stop()
        time.sleep(1)

        forward()
        time.sleep(2)
        stop()
        time.sleep(1)
        turnLeft()
        time.sleep(turnTiming)
        stop()
        time.sleep(1)

        forward()
        time.sleep(2)
        stop()
        time.sleep(1)
        turnRight()
        time.sleep(0.33)
        stop()
        time.sleep(2)
        forward()
        time.sleep(2)
        stop()
        time.sleep(1)
        turnLeft()
        time.sleep(0.33)
        stop()
        time.sleep(2)
        forward()
        time.sleep(2)
        stop()
        isForward = True
    stop()
    break

    # if detectWay() == "Forward":
    #     if isForward != True:
    #         forward()
    #         isForward = True
    # elif detectWay() == "Right":
    #     # print(detectWay())
    #     # stop()
    #     if isRight != True:
    #         turnCycle()
    #         isRight = True
    #     # isRight = False
    # elif detectWay() == "Left":
    #     c = 0
    #     # print(detectWay())
    #     # turnLeft()
    #     stop()
    # elif detectWay() == "Intersection":
    #     d = 0
    #     print(detectWay())
    #     stop()
    #     break
# while time.time() < t_end:
#     if detectWay() == "Forward":
#         if isForward != True:
#             forward()
#             isForward = True
#     elif detectWay() == "Right":
#         # print(detectWay())
#         # stop()
#         if isRight != True:
#             turnCycle()
#             isRight = True
#         # isRight = False
#     elif detectWay() == "Left":
#         c = 0
#         # print(detectWay())
#         # turnLeft()
#         stop()
#     elif detectWay() == "Intersection":
#         d = 0
#         print(detectWay())
#         stop()
#         break
