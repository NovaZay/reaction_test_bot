import pyautogui
import keyboard
# Import libraries
# pyautogui does the color recognition and the click (so basically the whole purpose of the program)
# keyboard is to detect if the F10 key is pressed and if so, stop the program

stop_key = "f10"

# desired position to check 314 415 (x, y) (change do desired location to check)
# green (75, 219, 106) (change to desired color to be checked for in the coordinates proporcionated) 

while True: # making a loop
    screenshot = pyautogui.screenshot()                     # taking a whole screenshot
    pixel_color = screenshot.getpixel((314, 415))           # getting the color of the pixel at desired location
    if keyboard.is_pressed(stop_key):                       # detect if the stop key is pressed
        break                                               # if so, stop the program
    if pixel_color == (75, 219, 106):                       #detect if the color is green
        pyautogui.click(314, 415)                           # if so, click
    else:                                                   # if not
        print("Cannot find the green pixel")                # print this