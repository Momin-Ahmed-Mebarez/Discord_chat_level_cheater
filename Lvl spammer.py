import pyautogui
import pyperclip
import time
import random
line_count = 0
msg_count = 0

with open("Arabic.txt", "r", encoding='utf-8') as read_file:
    word = read_file.readlines()
    read_file.close()

for line in word:
        if line != "\n":
            line_count += 1

pyautogui.click(1120,677)
while True:
    pyperclip.copy(word[random.randint(0, line_count - 1)])
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(1128,619)
    pyautogui.click(1311,590)
#    time.sleep(1)
    pyautogui.click(1140,640)
    time.sleep(1)
    pyautogui.click(1172,500)
    msg_count = msg_count + 1
    print(msg_count)
    time.sleep(1)
    pyautogui.hotkey("ctrl","pgdn")
    time.sleep(57)
    pyautogui.hotkey("ctrl","pgdn")
    time.sleep(1)    













































"""
old numbers
time.sleep(1)
time.sleep(1)        
time.sleep(1)
time.sleep(27)
time.sleep(1)
"""












"""
q_cd = 0
w_cd = 0

pyautogui.click(841,352)
while True:
    if w_cd <= 0:
        pyautogui.press('w')
        w_cd = 27
        
    if q_cd <= 0:
        pyautogui.press('q')
        q_cd = 9
        w_cd = w_cd - 1
    pyautogui.click(841,352)
    time.sleep(1)
    q_cd = q_cd - 1
    w_cd = w_cd - 1

    
#Q = 9
#W = 27
"""
