import pyautogui

import mouse
import keyboard
import numpy as np
import pygetwindow as gw
import pyscreenshot as ImageGrab
import win32gui
import csv
import random
import time
from PIL import ImageGrab
from PIL import Image
import cv2
import pyautogui
from ctypes import windll
import win32api, win32con
import win32gui
dc= windll.user32.GetDC(0)




success_counter=0
counter=0


def rgbint2rgbtuple(RGBint):
    return (RGBint // 256 // 256 % 256, RGBint // 256 % 256, RGBint % 256)


wow = gw.getWindowsWithTitle('WORLD OF WARCRAFT')[0]

wow.activate()
wow.moveTo(1, 1)

def searchBob():
    coordinates=[]
    imgCheckChange=pyautogui.screenshot('search.jpg', region=(750,250,800,400))
    img=cv2.imread('search.jpg')
    for px in range(1,len(img),1):
        for py in range(1,len(img[0]),1):
            if (img[px][py][2]>240):
                coordinates.append(px+250)
                coordinates.append(py+750)
                #print(coordinates)
                return coordinates


def success():
    intS=win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 256 , 228)
    intS=rgbint2rgbtuple(intS)
    #print("Success: ",intS)
    succ=False
    if (intS[0]<10 and intS[1]<10 and intS[2]>80):
        succ=True
    return succ





def getpixel(x,y):
    return windll.gdi32.GetPixel(dc,x,y)


for x in range (10000):
    counter+=1
    clickCoord=[]
    t0= time.clock()
    time.sleep(0.4)
    mouse.move(1,1)
    time.sleep(1)
    keyboard.press_and_release('0')
    time.sleep(2)
    clickCoord=searchBob()
    if (clickCoord==None):
        print("did not find anything...retrying")
        continue
    mouse.move(0,0)
    time.sleep(0.5)
    bite=False
    bobCheckCounter=0
    averageRed=[]
    while(bite==False):
        #print(clickCoord)
        imgCheckChange=pyautogui.screenshot('tempChange.jpg', region=(clickCoord[1]-37,clickCoord[0]-23,67,57))
        img=cv2.imread('tempChange.jpg')
        if bobCheckCounter<1:
            cv2.imwrite('abc{}.jpg'.format(x),img)         
        WhiteCounter=0
        for px in range(1,len(img),1):
            for py in range(1,len(img[0]),1):
                if img[px][py][2]>240:
                    WhiteCounter+=1
        print("WhiteCounter",WhiteCounter)
        if (bobCheckCounter > 2 and bobCheckCounter < 11):
            if (len(averageRed)<8):
                averageRed.append(WhiteCounter)
            ave=sum(averageRed)
            ave=ave/len(averageRed)
        bobCheckCounter+=1
        if bobCheckCounter>4:
            ### 0.3 --> 0.65, 04. --> 0.7
            if abs(WhiteCounter-ave)>ave*0.4:
                bite=True
                print("I Think i got something...")
            if (time.clock() - t0 > 29):
                print("Time ran out! restarting...")
                bite=True
        WhitePrev=WhiteCounter

    time.sleep(1.1)
    mouse.move(clickCoord[1],clickCoord[0])
    pyautogui.click(button='right')
    print("FoundIt")
    time.sleep(1.3)
    if success():
        success_counter+=1
    mouse.move(90,340)
    time.sleep(0.5)
    pyautogui.click(button='right')
    mouse.move(90,390)
    time.sleep(0.5)
    pyautogui.click(button='right')
    print("At try numer: ",counter)
    print("Catches: ",success_counter)
    print("Success rate: ", success_counter/counter)
    print("keep on going...")
    time.sleep(3.78)

        
hwnd = win32gui.FindWindow(None,"WORLD OF WARCRAFT")
print(hwnd)
win32gui.SetForegroundWindow(hwnd)
print(win32gui.GetWindowText(hwnd))
#win32gui.MoveWindow(hwnd, 0, 0, 1400, 1400, True)
#bbox = win32gui.GetWindowRect(hwnd)



    
