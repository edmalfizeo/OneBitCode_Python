import time

import pyautogui
from time import sleep

with open('../files/students_registration.txt', 'r', encoding='utf-8') as file:
    for line in file:
        student = line.split(',')[0]
        email = line.split(',')[1]
        age = line.split(',')[2]

        pyautogui.click(1109, 223, duration=1)
        # sleep(1)
        pyautogui.typewrite(student)
        pyautogui.click(1109, 251, duration=1)
        # sleep(1)
        pyautogui.typewrite(email)
        pyautogui.click(1109, 284, duration=1)
        # sleep(1)
        pyautogui.typewrite(age)
        # sleep(1)
        pyautogui.click(1017, 336, duration=0.5)
        sleep(1)

