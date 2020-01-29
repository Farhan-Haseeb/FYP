import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

TRIG = 40
ECHO = 38

gpio.setup(TRIG, gpio.OUT)
gpio.setup(ECHO, gpio.IN)


t_end = time.time() + 60 * 1


def Sonar():
    print("Detecting object, with stopping distance of 10cm")

    gpio.output(TRIG, False)
    # print("Waiting for Sensor to Settle")
    time.sleep(0.5)

    gpio.output(TRIG, True)
    time.sleep(0.0001)
    gpio.output(TRIG, False)
    while gpio.input(ECHO) == False:
        start = time.time()
    while gpio.input(ECHO) == True:
        end = time.time()
    sig_time = end-start
    # cm:
    distance = sig_time / 0.000058
    # print("Distance: {} cm".format(round(distance, 2)))
    print("Keep on Going...")
    if distance < 21:
        print("\nStop, object detected at {} cm !!!".format(round(distance, 2)))
        return True
       #  gpio.cleanup()
