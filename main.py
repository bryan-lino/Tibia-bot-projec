import ctypes
import time
import keyboard
import pyautogui
from screen import find_image, look_screen
import cv2
import numpy as np
from numpy import random

WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_MOUSEMOVE = 0x0200
MK_LBUTTON = 0x0001
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x202
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP = 0x205

F1 = 0x70
F2 = 0x71
F3 = 0x72
F4 = 0x73
F5 = 0x74
F6 = 0x75
F7 = 0x76
F8 = 0x77
F9 = 0x78
F10 = 0x79
F11 = 0x7A
F12 = 0x7B

np.food = ('images/fish.png', 'images/meat_1.png', 'images/meat_2.png', 'images/meat_3.png', 'images/meat_4.png', 'images/meat_5.png', 'images/ham_1.png', 'images/ham_2.png', 'images/ham_3.png', 'images/ham_4.png', 'images/ham_5.png')
np.water = ('images/water_0.png', 'images/water_1.png', 'images/water_2.png', 'images/water_3.png', 'images/water_4.png', 'images/water_5', 'images/water_6', 'images/water_7', 'images/water_8')
np.fishingRod = ('images/fishing_rod.png', 'images/fishing_rod2.png', 'images/fishing_rod3.png')
np.spear = ('images/spear_1.png', 'images/spear_2.png', 'images/spear_3.png', 'images/spear_4.png')

def send_message_keyboard(hwnd, key_code):
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
    time.sleep(0.2)
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)

# Works on any OT or Tibia Global (In Tibia Global you'll need to use OBS (SOURCE MODE))
## Put the name of the game window here
hwnd = ctypes.windll.user32.FindWindowW(0, 'Antiga - Baron')

def send_key_to_window(hwnd, scan_code):
    lParam_down = (1 << 0) | (scan_code << 16)
    lParam_up = (1 << 0) | (scan_code << 16) | (1 << 30) | (1 << 31)
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, scan_code, lParam_down)
    time.sleep(0.2)
    ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, scan_code, lParam_up)

def moveTo(hwnd, x, y):
    x = int(x)
    y = int(y)
    lParam = (y << 16) | x
    ctypes.windll.user32.SendMessageW(hwnd, WM_MOUSEMOVE, MK_LBUTTON, lParam)

def click(hwnd, x, y, button='left'):
    x = int(x)
    y = int(y)
    lParam = (y << 16) | x
    if button == 'left':
        ctypes.windll.user32.SendMessageW(hwnd, WM_LBUTTONDOWN, 1, lParam)
        time.sleep(0.015) 
        ctypes.windll.user32.SendMessageW(hwnd, WM_LBUTTONUP, 0, lParam)
        return
    ctypes.windll.user32.SendMessageW(hwnd, WM_RBUTTONDOWN, 0, lParam)
    time.sleep(0.015)
    ctypes.windll.user32.SendMessageW(hwnd, WM_RBUTTONUP, 0, lParam)

def drag(hwnd, x, y, button='left'):
    x = int(x)
    y = int(y)
    lParam = (y << 16) | x
    if button == 'left':
        ctypes.windll.user32.SendMessageW(hwnd, WM_LBUTTONDOWN, 1, lParam)
        return
    ctypes.windll.user32.SendMessageW(hwnd, WM_RBUTTONDOWN, 0, lParam)

def release(hwnd, x, y, button='left'):
    x = int(x)
    y = int(y)
    lParam = (y << 16) | x
    if button == 'left':
        ctypes.windll.user32.SendMessageW(hwnd, WM_LBUTTONUP, 0, lParam)
        return
    ctypes.windll.user32.SendMessageW(hwnd, WM_RBUTTONUP, 0, lParam)

keyboard.wait('h')
while True:
    
    ##AUTO MANA TRAIN/RUNE MAKER
    # print('waiting...')
    # time.sleep(5)
    # print('using magic...')
    # send_message_keyboard(hwnd, F4)
    
    ##AUTO EAT FOOD
    # time.sleep(5)
    # print('eating...')
    # img = look_screen()
    # result = find_image(img, np.food)
    # print('result', result)
    # if result: 
    #     moveTo(hwnd, result[0], result[1])
    #     click(hwnd, result[0], result[1], 'right')

    # # AUTO FISHER
    # time.sleep(0.3)
    # print('using rod...')
    # img = look_screen()
    # result = find_image(img, np.fishingRod)
    # print('result', result)
    # if result: 
    #     moveTo(hwnd, result[0], result[1])
    #     click(hwnd, result[0], result[1], 'right')
    # time.sleep(0.3)
    # print('fishing...')
    # img = look_screen()
    # result = find_image(img, np.water)
    # print('result', result)
    # if result: 
    #     moveTo(hwnd, result[0], result[1])
    #     click(hwnd, result[0], result[1], 'left')

    # #PICK UP SPEARS
    time.sleep(0.3)
    img = look_screen()
    result = find_image(img, np.spear)
    print('spear found', result)
    if result: 
        moveTo(hwnd, result[0], result[1])
        drag(hwnd, result[0], result[1], 'left')
        print('pickin up the spear')
        time.sleep(0.3)
        moveTo(hwnd, 1590,442)
        release(hwnd, result[0], result[1], 'left')
