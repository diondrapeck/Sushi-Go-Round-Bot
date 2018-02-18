"""

game website: http://armorgames.com/play/124/sushi-go-round 

All coordinates assume a screen resolution of 1280x1024 and Chrome 
maximized with the Bookmarks Toolbar enabled.

Down key has been hit 2 times to center play area in browser.

"""

from PIL import ImageGrab
import os
import time
from ctypes import windll
import win32api, win32con

# make PIL DPI-aware, so entire screen is grabbed
user32 = windll.user32
user32.SetProcessDPIAware()

# Globals
x_pad = 469
y_pad = 204

def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 956, y_pad + 716)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    pass

if __name__ == '__main__':
    main()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print "Click."

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'

def mousePos(cord):
    win32api.SetCursorPos(x_pad + cord[0], y_pad + cord[1])
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y
