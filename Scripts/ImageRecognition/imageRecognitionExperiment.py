from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#Command for coordinates and rgb: pyautogui.displayMousePosition()



while 1:
    if pyautogui.locateOnScreen('PlayButton.png',region=(1477,901,430,170)) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
        
        
