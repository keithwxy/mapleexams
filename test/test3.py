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

print(pag.locateOnScreen("img/rune.png", region=(0, 0, 400, 200), confidence=0.90, grayscale=True))
