"""

game website: http://armorgames.com/play/124/sushi-go-round 

All coordinates assume a screen resolution of 1280x1024 and Chrome 
maximized with the Bookmarks Toolbar enabled.

"""

from PIL import ImageGrab
import os
import time
from ctypes import windll

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
    screenGrab()

if __name__ == '__main__':
    main()
