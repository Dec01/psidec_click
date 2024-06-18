import numpy as np
from mss import mss
import pyautogui as pg
import cv2
import keyboard

isClicking = False
isWindow = False

def status_window(status):
    return status


monitor = {
    "left": 40,
    "top": 40,
    "width": 350,
    "height": 600,
}


def find_color(our_color, monitor={}):
    m = mss()
    img = m.grab(monitor)
    img_arr = np.array(img)
    our_map = (our_color[2], our_color[1], our_color[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd


def clicker_winodw():
    while True:
        if isWindow:
            sct = mss()
            sct_img = sct.grab(monitor)
            cv2.imshow('screen', np.array(sct_img))
            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                cv2.destroyAllWindows()
                break



def set_window():
    global isWindow
    if isWindow:
     isWindow = False
    else:
        isWindow = True


color_arr3 = [[124, 255, 30], [63, 219, 0], [197, 255, 148], [230, 254, 145], [209, 254, 133], [205, 220, 0],
              [203, 227, 0], [90, 235, 17], [128, 242, 84], [85, 204, 220], [84, 160, 220], [82, 207, 20]]


def set_clicker():
    global isClicking
    if isClicking:
     isClicking = False
    else:
        isClicking = True

keyboard.add_hotkey('Alt + c', set_clicker)
keyboard.add_hotkey('Alt + w', set_window)

def clicker_tap():
    while True:
        if isClicking:
            for i in color_arr3:
                result = find_color(i, monitor)
                if result.__len__():
                    x = result[0][1] + monitor.get('left')
                    y = result[0][0] + monitor.get('top')
                    pg.click(x, y)

