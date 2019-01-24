from pynput.mouse import Button, Controller
import time


mouse = Controller()

time.sleep(5) # 10 second time to set mouse in appropriate position
for i in range(50):
    mouse.click(Button.left)
    time.sleep(.2)
