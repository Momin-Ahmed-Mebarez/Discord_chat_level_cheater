import pyautogui
import pyperclip
import time
import random


def start():
    line_count = 0
    msg_count = 0
    #A timer to give a chance to open the page
    time.sleep(2)
    
    #Reading the list file
    with open("Arabic.txt", "r", encoding='utf-8') as read_file:
        word = read_file.readlines()
        read_file.close()
        
    #Getting the number of lines in the list
    for line in word:
            if line != "\n":
                line_count += 1
                
    #Clicking on page to get focus (The number need to be changed depending on your screen (x,y))
    pyautogui.click(1120,677)
    
    while True:
        
        #Chosing a random word to put in clipboard
        pyperclip.copy(word[random.randint(0, line_count - 1)])

        #Sending the word 
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")

        #A timer to avoid beign flagged as spam (the number can be lowerd)
        time.sleep(57)







if __name__ == "__main__":
    start()









