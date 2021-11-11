import pyautogui
import keyboard
from ctypes import windll
dc = windll.user32.GetDC(0)

colour = 0
currentMouseX, currentMouseY = pyautogui.position()
while True:
    """if keyboard.is_pressed("q"):
        prev_colour = colour
        colour = windll.gdi32.GetPixel(dc, currentMouseX, currentMouseY)
        if colour != 3548878:
            pyautogui.click()
            prev_colour = colour
    else:
        currentMouseX, currentMouseY = pyautogui.position()"""
    colour = windll.gdi32.GetPixel(dc, currentMouseX, currentMouseY)
    currentMouseX, currentMouseY = pyautogui.position()
    print(colour, currentMouseX, currentMouseY)
    #  0 183
    #  1893 985

