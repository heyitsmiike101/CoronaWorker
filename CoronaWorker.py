version = 2.41

import pyautogui #Mouse Library: pip install pyautogui
import json
import time
import datetime
from random import randint
from pynput.keyboard import Key, Controller #Keyboard Library: pip install pynput. if issues persist use pip install pynput=1.6.8

#V2.3:   Added more logging. Prints the seconds every 20 seconds instead of 10. add the choice of moving mouse, pressing control, or both.
#V2.4:   Added the ability to pause activity without closing the program.
def secondCountdown(length, message,countdown = True):
    try:
        for i in range(int(length), 0, -1):
            if i%length == 0:
                print(i, message)
            elif i < 4 and countdown:
                print(i, message)
            time.sleep(1)
            
    except KeyboardInterrupt:
        return False
    return True

def simulateMovement(x,y,key, moveMouse, pressButton):
    keyboard = Controller()
    if moveMouse: 
        pyautogui.moveRel(x, y, duration = .2)
        print("Mouse: (" + str(x) + "," + str(y) + ")")
        pyautogui.moveRel(-x, -y, duration = .1)
        print("Mouse: (" + str(-x) + "," + str(-y) + ")")
    
    #Presses control on the keyboard.
    if pressButton:
        print("Button press")
        keyboard.press(key)
        keyboard.release(key)

def readSettingsJSON():
    filename = "afkSettings.txt"
    data = {'startTime': '8:00',
            'endTime': '17:00',
            'moveInterval': 60,
            'mouseMovement': False,
            'maxPixelsToMove': 10,
            'keyPress': True}

    #If the filename is found, fill in the custom data. Otherwise fill in default settings
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
        json_file.close()
    except FileNotFoundError:
        with open(filename, 'w') as outfile:  
            json.dump(data, outfile)
        outfile.close()

    return data

def main():
    settings = readSettingsJSON()
    moveMouse = settings["mouseMovement"]
    pressButton = settings["keyPress"]
    moveInterval = settings["moveInterval"]
    totalTime = 0
    print("###########################################")
    print("###########################################")
    print("Corona Worker - Version:", version)
    print("      ,-^-.          ,-^-.   ")
    print("      |\/\|          |\/\|   ")
    print("      `-V-'          `-V-'   ")
    print("        H              H     ")
    print("        H              H     ")
    print("        H              H     ")
    print('     .-;":-.        .-;":-.  ')
    print("   /,'|  `; \     /,'|  `; \ ")
    print("Program is set to run", settings["startTime"], "-", settings["endTime"])
    print("If you want to change the start time, \nend time, move internal and other settings, \nopen afkSettings.txt")
    print("###########################################")
    print("###########################################\n\n")
    
    while True:
        newSettings = readSettingsJSON()
        settings = newSettings
        moveMouse = settings["mouseMovement"]
        pressButton = settings["keyPress"]
        moveInterval = settings["moveInterval"]
        maxPixelsToMove = settings["maxPixelsToMove"]

        x = randint(3,maxPixelsToMove)
        y = randint(3,maxPixelsToMove)
        currentTime = datetime.datetime.now()
        currentDate = currentTime.strftime("%Y %m %d ")
        startTime = datetime.datetime.strptime(currentDate + settings["startTime"], "%Y %m %d %H:%M")
        endTime = datetime.datetime.strptime(currentDate + settings["endTime"], "%Y %m %d %H:%M")
        StartTimeDiff = (currentTime - startTime) #Shows as negative days when current time is before start time.
        endTimeDiff = (currentTime - endTime)#Shows as negative days when current time is before end time.

        #program wont start until a certain time
        if StartTimeDiff.days < 0:
            print("Program won't start until ", startTime.strftime("%H:%M"))
            secondCountdown(moveInterval/4, "Seconds until checking again.", False)
            continue
        
        #program quits after a certain time
        elif endTimeDiff.days > -1:
            secondCountdown(moveInterval, "Seconds until checking if program will unpause. This will happen tomorrow", False)
            continue
            #break
            
        #otherwise the program does movement.

        #the interval that the mouse moves and left control is pressed.
        secondCountdown(moveInterval, "Seconds until movement. ")

        #Moves the mouse a random amount and presses left control.
        simulateMovement(x,y,Key.shift, moveMouse, pressButton)
        totalTime += moveInterval
        #Prints the toal runtime very 5 minutes.
        printInterval = 60*5
        if totalTime%printInterval == 0:
            print("Total Runtime :", int(totalTime/60),"minutes")

if __name__== "__main__":
    try:
        main()
    except Exception as e:
        print(e)
