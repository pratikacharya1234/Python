from bumblebee import Mouse, Keyboard
import random
import time

import pyautogui

mouse = Mouse()
keyboard = Keyboard()
max_x, max_y = pyautogui.size()
for i in range(100):
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    mouse.move(x, y)
    time.sleep(0.2)