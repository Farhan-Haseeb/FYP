import RPi.GPIO as GPIO
import time

s0 = 35
s1 = 33
s2 = 31
s3 = 29
led = 36
signal = 37  # out pin
NUM_CYCLES = 10


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(signal, GPIO.IN)
    GPIO.setup(s0, GPIO.OUT)
    GPIO.setup(s1, GPIO.OUT)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    GPIO.setup(led, GPIO.OUT)

    # GPIO.output(s0, True)
    # GPIO.output(s1, True)
    # GPIO.output(led, True)
    print("\n")


def loop():
    temp = 1
    # while(1):
    print("\n")
    GPIO.output(s2, False)
    GPIO.output(s3, False)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    red = NUM_CYCLES / duration

    GPIO.output(s2, False)
    GPIO.output(s3, True)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration

    GPIO.output(s2, True)
    GPIO.output(s3, True)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration

    if green < 7000 and blue < 7000 and red > 12000:
        print("red")
        temp = 1
    elif red < 12000 and blue < 12000 and green > 12000:
        print("green")
        temp = 1
    elif green < 7000 and red < 7000 and blue > 12000:
        print("blue")
        temp = 1
    elif red > 10000 and green > 10000 and blue > 10000 and temp == 1:
        print("place the object.....")
        temp = 0
    else:
        print("Red: {}\nGreen: {}\nBlue: {}".format(red, green, blue))



def colors(red, green, blue):
    if green < 7000 and blue < 7000 and red > 12000:
        print("red")
        temp = 1
    elif red < 12000 and blue < 12000 and green > 12000:
        print("green")
        temp = 1
    elif green < 7000 and red < 7000 and blue > 12000:
        print("blue")
        temp = 1
    elif red > 10000 and green > 10000 and blue > 10000 and temp == 1:
        print("place the object.....")
        temp = 0
    else:
        print("Red: {}\nGreen: {}\nBlue: {}\n".format(red, green, blue))

def red():
    # red
    GPIO.output(s2, False)
    GPIO.output(s3, False)
    red = getData()

    # blue
    GPIO.output(s2, False)
    GPIO.output(s3, True)
    blue = getData()

    # green
    GPIO.output(s2, True)
    GPIO.output(s3, True)
    green = getData()

    colors(red, green, blue)
    # print("Red: {}\nGreen: {}\nBlue: {}".format(red, green, blue))

def getData():
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    return NUM_CYCLES / duration

def loop2():
    GPIO.output(s2, False)
    GPIO.output(s3, False)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start  # seconds to run for loop
    red = NUM_CYCLES / duration  # in Hz
    # print("red value - ", red)

    GPIO.output(s2, False)
    GPIO.output(s3, True)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    # print("blue value - ", blue)

    GPIO.output(s2, True)
    GPIO.output(s3, True)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    # print("green value - ", green)
    time.sleep(2)

    if green < 7000 and blue < 7000 and red > 12000:
        print("red")
        temp = 1
    elif red < 12000 and blue < 12000 and green > 12000:
        print("green")
        temp = 1
    elif green < 7000 and red < 7000 and blue > 12000:
        print("blue")
        temp = 1
    elif red > 10000 and green > 10000 and blue > 10000 and temp == 1:
        print("place the object.....")
        temp = 0
    else:
        print("Red: {}\nGreen: {}\nBlue: {}\n".format(red, green, blue))


def endprogram():
    GPIO.cleanup()


setup()
try:
    # loop()
    # loop2()
    red()
except KeyboardInterrupt:
    endprogram()
