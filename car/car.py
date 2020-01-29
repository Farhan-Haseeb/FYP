# For detecting pathway
from ir import detectWay
# Motor controls
from motors import forward, reverse, turnLeft, turnRight, stop
# Object Detection
from sonar import Sonar
import time

# Time for turn cycle
turningTime = time.time() + 50 * 0.1

# Global run
run = True

#Turning Logic
def turnCycle(turn):
  # Stop car
  stop()
  # Wait for 2 second
  time.sleep(1)
  # Turn car, according to args passed
  while time.time() < turningTime:
    turn()
    break
  # Stop car
  stop()

while run:
  if detectWay() == 'Forward':
    forward()
  elif detectWay() == 'Right':
    turnCycle(turnRight)
  elif detectWay() == 'Left':
    turnCycle(turnLeft)
  elif detectWay() == 'Intersection':
    print('Intersection')
    stop()
    run = False