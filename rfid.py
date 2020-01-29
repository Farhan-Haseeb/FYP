import evdev
from select import select

# Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader
def getDevice():
  devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
  for device in devices:
      if device.name == "Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader":
        return device
      return False

device = getDevice()

if device:
  dev = device

  rfid_presented = ""

  keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

  while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
      if event.type==1 and event.value==1:
        if event.code==28:
          #Here RFID will be detected.
         print(rfid_presented)
         rfid_presented = ""
        else:
          rfid_presented += keys[event.code]
else:
  print("RFID Reader not Found")

