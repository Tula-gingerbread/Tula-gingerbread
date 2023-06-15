import pyautogui
import psutil
import os
from time import sleep

input_text = input('Enter the text for spam. Only English and special characters: ')
input_delay = input('Enter delay for sending message: ')
print('Dont move cursor. Start in 3 seconds')
print('To stop spam execution, close cmd.exe')
sleep(3)

for proc in psutil.process_iter(['pid', 'name']):
    if proc.name() == 'Discord.exe':
        # Открытие процесса по PID
        os.startfile(proc.exe())
        sleep(1.5)
        break

pyautogui.FAILSAFE=False

pyautogui.move(-1100, -1100)
pyautogui.move(403, 995)
pyautogui.click()
while True:
    pyautogui.typewrite(f"{input_text}")
    pyautogui.press('enter')
    sleep(float(input_delay))