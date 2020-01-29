import keyboard

while True:
	if keyboard.is_pressed("w"):
		print('Forward')
	if keyboard.is_pressed('a'):
		print('Left')
	if keyboard.is_pressed('d'):
		print('Right')
	if keyboard.is_pressed('q'):
		print('exiting...')
		break
