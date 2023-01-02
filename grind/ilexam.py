from time import sleep
from interception import *
import pydirectinput as pdi
import random
from pynput import keyboard


def jump(direction):
    pdi.keyDown(direction)
    pdi.press("space")
    pdi.keyUp(direction)

def small_sleep():
    sleep(random.randint(1, 3)/100)


def med_sleep():
    sleep(random.randint(5, 15)/100)


def long_sleep():
    sleep(random.randint(7,20)/100)

def press(key):
    pdi.keyDown(key)
    med_sleep()
    pdi.keyUp(key)


def hold(key, duration):
    pdi.keyDown(key)
    sleep(duration)
    pdi.keyUp(key)

def reset():
    if random.randint(0,2):
        jump("right")
    else:
        jump("left")
    pdi.press("up")
    pdi.press("down")
    pdi.keyDown("right")
    long_sleep()
    pdi.keyUp("right")
    if random.randint(0,2):
        jump("right")
    else:
        jump("left")
    pdi.keyDown("left")
    long_sleep()
    long_sleep()
    pdi.keyUp("left")

def on_press(key):
    if key == keyboard.Key.esc:
        pdi.keyUp("left")
        pdi.keyUp("right")
        exit()

sleep(1)
y = 0

while True:
    if y > 5:
        z = random.randint(0,4)
        if z == 0:
            press("enter")
            pdi.typewrite("HAHHAHAHHA")
            press("enter")
        if z == 1:
            press("enter")
            pdi.typewrite("xd i fk ur mother")
            press("enter")
        if z == 2:
            press("enter")
            pdi.typewrite("LOLOLOLOL")
            press("enter")     
        if z == 3:
            press("enter")
            pdi.typewrite("sure")
            press("enter")   
        y = 0        
    if random.randint(0,10) >  6:
        press("x")
        sleep(0.6)
        press("space")
        press("z")
    med_sleep()
    # Start
    if random.randint(0,1):
        pdi.press("right")
    else:
        pdi.press("left")
    med_sleep()
    for x in range(0, random.randint(2, 6)):
        press("d")
        small_sleep()
    pdi.keyDown("down")
    sleep(0.1)
    press("space")
    press("space")
    sleep(0.02)
    pdi.keyUp("down")
    press("end")

    if random.randint(0,2):
        pdi.press("right")
    else:
        pdi.press("left")
    med_sleep()
    for x in range(0, random.randint(2, 6)):
        press("d")
        small_sleep()
    pdi.press("space")
    pdi.keyDown("up")
    pdi.press("space")
    pdi.press("space")
    press("shift")
    pdi.keyUp("up")

    med_sleep()
    #y += 1