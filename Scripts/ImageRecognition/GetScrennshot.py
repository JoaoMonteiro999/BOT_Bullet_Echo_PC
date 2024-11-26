from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#Command for coordinates and rgb: ccc
#Play button box X: 1477 Y:  901



iml = pyautogui.screenshot(region=(1477,901,430,170))
iml.save(r"C:\Users\Utilizador\Desktop\Projeto Bot Bullet Echo\Scripts\ImageRecognition\savedimage.png")
