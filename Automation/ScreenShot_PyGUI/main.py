import pyautogui
import time

# Take a screenshot
# pyautogui.screenshot('screenshot.png')

pyautogui.moveTo(1800, 28, 1)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.screenshot('screenshot2.png')