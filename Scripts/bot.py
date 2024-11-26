from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con




# Always play on fullscreen!
# Coordinates on fullscreen:
# X for closing the AD coordinates: X: 1468 Y:  207 RGB: (255, 255, 255)
# Another X for closing AD coordinates: X: 1443 Y:  229 RGB: (  4,  60, 134)
# Confirmation button after some ADs coordinates:  X:  763 Y:  770 RGB: (255, 255, 255)
# Collect button after match coordinates: X:  962 Y:  939 RGB: (255, 255, 255)
# Results afters death coordinates: X:  225 Y:  994 RGB: (255, 255, 255)
# Dont Save coordinates: X:  633 Y:  806 RGB: (255, 255, 255)
# Random place to leave league leaderboard coordinates: X:  934 Y:    8
# X to leave contract progress window coordinates: X: 1838 Y:   73 RGB: ( 10, 140, 237)
# level up  : X: 1266 Y:  945 RGB: (255, 255, 255)




def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)




def deleteAd():
    #Deletes 2 straight up ads
    for  x in range (0,1,2):
        
        if pyautogui.pixel(1468,207) [0] == 255:
            if pyautogui.pixel(1468,207) [1] == 255:
                if pyautogui.pixel(1468,207) [2] == 255:
                    click(1468,207)
                    print('clicked "X" to leave ad')
                    time.sleep(2)
                    #Confirm the ad closing
                    if pyautogui.pixel(763,770) [0] == 255:
                        if pyautogui.pixel(763,770) [1] == 255:
                            if pyautogui.pixel(763,770) [2] == 255:
                                click(763,770)
                                print('clicked "Yes" to confirm closing the ad')
                                time.sleep(2)

                    else:
                        print ('couldnt click "Yes" to close the ad')      
        else:
            print ('couldnt click "X to leve ad')


        if pyautogui.pixel(1443,229) [0] == 4:
            if pyautogui.pixel(1443,229) [1] == 60:
                if pyautogui.pixel(1443,229) [2] == 134:
                    click(1443,229)
                    print('clicked "X" to leave ad')
                    time.sleep(2)
                    #Confirm the ad closing
                    if pyautogui.pixel(763,770) [0] == 255:
                        if pyautogui.pixel(763,770) [1] == 255:
                            if pyautogui.pixel(763,770) [2] == 255:
                                click(763,770)
                                print('clicked "Yes" to confirm closing the ad')
                                time.sleep(2)

                    else:
                        print ('couldnt click "Yes" to close the ad') 
        else:
            print ('couldnt click "X to leve ad')
        


        if pyautogui.pixel(1838,73) [0] == 10:
            if pyautogui.pixel(1838,73) [1] == 140:
                if pyautogui.pixel(1838,73) [2] == 237:
                    click(1838,73)
                    print('clicked "X" to leave ad')
                    click(934,8)


            

def startGame():
    #Start a game
    if pyautogui.pixel(1624,985) [0] == 255:
        if pyautogui.pixel(1624,985) [1] == 255:
            if pyautogui.pixel(1624,985) [2] == 255:
                click(1624,985)
                print('clicked in "Play" button')
                time.sleep(1)
                click(1624,985)
                #onGame = True
                #keyboard.press('E')
                #time.sleep(0.05)
                #keyboard.release('E')
                #inGame(onGame)
    else:
        print('couldnt start the game')

    time.sleep(3)
    click(1624,985)
    if pyautogui.pixel(1266,945) [0] == 255:
        if pyautogui.pixel(1266,945) [1] == 255:
            if pyautogui.pixel(1266,945) [2] == 255:
                click(1266,945)
                print('clicked in "OK" button for leveling up')
    time.sleep(3)
    click(1624,985)
    if pyautogui.pixel(1266,945) [0] == 255:
        if pyautogui.pixel(1266,945) [1] == 255:
            if pyautogui.pixel(1266,945) [2] == 255:
                click(1266,945)
                print('clicked in "OK" button for leveling up')

    
    #Checks if game is over, if it is leaves
    #while onGame := True:
        

#def inGame()
        #Bot gameplay here:


        




        #if pyautogui.pixel(1624,985) [0] == 255:
            #if pyautogui.pixel(1624,985) [1] == 255:
                #if pyautogui.pixel(1624,985) [2] == 255:
                  #  click(1624,985)
                    #print('clicked in "Play" button')
                   # time.sleep(1)



#Temporary
def leaveGame():
    onGame = True
    while onGame == True:
        time.sleep(2)

        keyboard.press('W')
        time.sleep(0.5)
        keyboard.release('W')
        
        if pyautogui.pixel(633,806) [0] == 255:
            if pyautogui.pixel(633,806) [1] == 255:
                if pyautogui.pixel(633,806) [2] == 255:
                    click(633,806)
                    print('clicked "Dont Save" after the match')


        if pyautogui.pixel(962,939) [0] == 255:
            if pyautogui.pixel(962,939) [1] == 255:
                if pyautogui.pixel(962,939) [2] == 255:
                    click(962,939)
                    print('clicked "Collect" after the match')
                    onGame = False
                    time.sleep(2)
                    click(934,8)



#Main
while keyboard.is_pressed('k') == False:
    #Stars
    #Time to Alt-Tab
    time.sleep(4)
    #Deletes 2 straight up ads
    deleteAd()
    #Starts a game
    startGame()

    leaveGame()
