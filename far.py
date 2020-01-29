import RPi.GPIO as GPIO
import curses

screen = curses.initscr()
curses.cbreak()
curses.noecho()
screen.keypad(True)

motor_power1 = 12
motor_power2 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(motor_power1,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(motor_power2, GPIO.OUT)

def up():
	GPIO.output(11, True)
	GPIO.output(15, True)
	GPIO.output(7,False)
	GPIO.output(13,False)
def down():
	GPIO.output(7,True)
	GPIO.output(13,True)
	GPIO.output(11,False)
	GPIO.output(15,False)
def left():
	GPIO.output(11,True)
	GPIO.output(13,True)
	GPIO.output(7,False)
	GPIO.output(15,False)
def right():
	GPIO.output(11,False)
	GPIO.output(13,False)
	GPIO.output(7,True)
	GPIO.output(15,True)

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_UP:
			up()
		elif char == curses.KEY_DOWN:
			down()

finally:
	curses.nobreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()
