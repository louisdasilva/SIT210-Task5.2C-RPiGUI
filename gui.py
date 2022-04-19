# A GUI to switch between a red, blue and green LED light from a Raspberry Pi board
# Code made with reference to and adaptations from:
# https://coderslegacy.com/python/python-gui/python-tkinter-radio-button/

import RPi.GPIO as GPIO
from time import sleep
from tkinter import *

GPIO.setmode(GPIO.BCM)

RED = 16
BLUE = 20
GREEN = 21

colours = [RED, BLUE, GREEN]

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

def led_switcher():
    root = Tk()
    root.title("Switch")

    # create main window
    main_menu = Frame(root)
    main_menu.pack()
    label = Label(main_menu, text = "LED Select Switch")
    label.pack(pady = 10)

    light = IntVar()
    def switch():
        switch_on_led(light.get())

    # create all LED's off button
    off_button = Radiobutton(root, text = "Off", variable = light, value = 0, command = switch)
    off_button.pack(side = LEFT)

    # create red LED radio button
    red_button = Radiobutton(root, text = "Red", variable = light, value = RED, command = switch)
    red_button.pack(side = LEFT)

    # create green LED radio button
    green_button = Radiobutton(root, text = "Green", variable = light, value = GREEN, command = switch)
    green_button.pack(side = LEFT)

    # create blue LED radio button 
    blue_button = Radiobutton(root, text = "Blue", variable = light, value = BLUE, command = switch)
    blue_button.pack(side = LEFT)

    root.mainloop()

def switch_on_led(led_colour):
    for x in colours:
        GPIO.output(x, GPIO.LOW)
    if(not(led_colour == 0)):
        GPIO.output(led_colour, GPIO.HIGH)

try:
    led_switcher()
finally:
    for x in colours:
        GPIO.output(x, GPIO.LOW)
    GPIO.cleanup()
