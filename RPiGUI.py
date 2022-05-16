#!/usr/bin/python3

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

blue=LED(14)
yellow=LED(15)
green=LED(18)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


### Event Functions ###
def pressed_blue():
    green.off()
    greenButton["text"]="Turn green LED on"

    yellow.off()
    yellowButton["text"]="Turn yellow LED on"
    
    if blue.is_lit:
        blue.off()
        blueButton["text"]="Turn blue LED on"
    else:
        blue.on()
        blueButton["text"]="Turn blue LED off"

def pressed_yellow():
    green.off()
    greenButton["text"]="Turn green LED on"

    blue.off()
    blueButton["text"]="Turn blue LED on"

    if yellow.is_lit:
        yellow.off()
        yellowButton["text"]="Turn yellow LED on"
    else:
        yellow.on()
        yellowButton["text"]="Turn yellow LED off"

def pressed_green():
    yellow.off()
    yellowButton["text"]="Turn yellow LED on"

    blue.off()
    blueButton["text"]="Turn blue LED on"

    if green.is_lit:
        green.off()
        greenButton["text"]="Turn green LED on"
    else:
        green.on()
        greenButton["text"]="Turn green LED off"

def close():
    GPIO.cleanup()
    win.destroy()


### WIDGETS ###

# Button, triggers the connected command when it is pressed
blueButton = Button(win, text='Turn blue LED on', font=myFont, command=pressed_blue, bg='bisque2', height=1, widt>
blueButton.grid(row=0,column=1)

yellowButton = Button(win, text='Turn yellow LED on', font=myFont, command=pressed_yellow, bg='bisque2', height=1>
yellowButton.grid(row=1,column=1)

greenButton = Button(win, text='Turn green LED on', font=myFont, command=pressed_green, bg='bisque2', height=1, w>
greenButton.grid(row=2,column=1)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=4, column=1)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops forever
