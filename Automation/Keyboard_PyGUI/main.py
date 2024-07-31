import pyautogui
import time

# 1 - Press the key
pyautogui.press('winleft')
time.sleep(1)

# 2 - write
pyautogui.write('calculadora')
time.sleep(1)

# 3 - Press the key
pyautogui.press('enter')
time.sleep(1)

# 4 - Open task manager
pyautogui.hotkey('ctrl', 'shift', 'esc')
time.sleep(1)

with pyautogui.hold('winleft'):
    pyautogui.press('left')
    pyautogui.press('enter')
time.sleep(1)