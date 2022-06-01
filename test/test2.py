import cv2

from sewar.full_ref import mse, psnr, rmse, uqi, ssim, ergas, scc, rase, sam, msssim, vifp
import pygetwindow
import pyautogui as pag
import pydirectinput as pdi
from PIL import Image
import random
from time import sleep
import psutil

random.seed(98039704)

def small_sleep():
    sleep(random.randint(1, 3)/100)


def med_sleep():
    sleep(random.randint(4, 6)/100)


def press(key):
    pdi.keyDown(key)
    small_sleep()
    pdi.keyUp(key)


def hold(key, duration):
    pdi.keyDown(key)
    sleep(duration)
    pdi.keyUp(key)

uparr = "arrow/up.png"
dwarr = "arrow/dw.png"
ltarr = "arrow/lt.png"
rtarr = "arrow/rt.png"
challenge = "arrow/challenge.png"
sleep(2)
answers = {}
if not pag.locateOnScreen("img/photo_viewer.png", confidence=0.99, region=(0, 0, 500, 400)):
            # Locate window
            viewer_cords = pag.locateOnScreen("img/photo_color.png", confidence=0.9)
            pag.click(viewer_cords.left+5, viewer_cords.top+5)

uplist = pag.locateAllOnScreen(uparr, confidence=0.85)
if uplist:
    for i in uplist:
        answers[i.left] = "up" # 72 
dwlist = pag.locateAllOnScreen(dwarr, confidence=0.85)
if dwlist:
    for i in dwlist:
        answers[i.left] = "down" # 80
ltlist = pag.locateAllOnScreen(ltarr, confidence=0.85)
if ltlist:
    for i in ltlist:
        answers[i.left] = "left" # 75
rtlist = pag.locateAllOnScreen(rtarr, confidence=0.85)
if rtlist:
    for i in rtlist:
        answers[i.left] = "right" # 77
# Close image
for proc in psutil.process_iter():
    if proc.name() == "Microsoft.Photos.exe":
        proc.kill()
print(answers)
# Clean dictionary
prevx = 0
for i in sorted(answers.keys()):
    if i - prevx < 20:
        answers.pop(i)
    prevx = i
print(len(answers))
print(answers)