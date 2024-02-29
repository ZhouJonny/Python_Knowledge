"""
Move the mouse every five seconds, so that the computer will never sleep
"""
import logging
import random
import time

import pyautogui

while True:
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    pyautogui.moveRel(x, y)
    print(f'current location---x:{x} y:{y}')
    time.sleep(5)


