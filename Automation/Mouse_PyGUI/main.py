import time

import pyautogui

# 1 - Get the screen size
print(pyautogui.size())

# 2 - Get the current mouse position
print(pyautogui.position())

# 3 - See the mouse position in real time
# Python
# from pyautogui import mouseInfo
# mouseInfo()

# 4 - Move the mouse to a specific position
pyautogui.moveTo(282, 93)
time.sleep(1.5)
pyautogui.click()
pyautogui.scroll(-900)
