from time import sleep
import pyautogui as pag
import pydirectinput as pdi
import random

# Find stage
sleep(1)

stage = pag.locateOnScreen("stage.png", confidence=0.90)
if (stage):
    print("Stage found")
aa = pag.screenshot("test.png", region=(stage.left, stage.top-200, 150, 200))
while True:
    while (pag.locateOnScreen("fever.png", region=(stage.left-125, stage.top+10, 300, 900), confidence= 0.70, grayscale=True)):
        pdi.press("space")
    if pag.locateOnScreen("left.png", region=(stage.left, stage.top-200, 150, 200), confidence= 0.60):
        print("l")
        pdi.press("left")
    elif pag.locateOnScreen("up.png", region=(stage.left, stage.top-200, 150, 200), confidence= 0.60):
        pdi.press("up")
        print("u")
    elif pag.locateOnScreen("right.png", region=(stage.left, stage.top-200, 150, 200), confidence= 0.60):
        pdi.press("right")
        print("r")
    