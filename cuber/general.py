import sys
import pyautogui as pag
import random
from time import sleep
import pydirectinput as pd
from interception import *

# Paths
sbimg = "img/blossom.png"
ivimg = "img/inventory.png"
cube  = "img/cube.png"
okbut = "img/okbut.png"
res = "img/res.png"

def small_sleep():
    sleep(random.randint(1, 3)/100)


def med_sleep():
    sleep(random.randint(4, 6)/100)


def oneMoreTime(left, top):
        oneMore = pag.locateOnScreen('img/onemore.png', region=(left, top, 670, 385))
        if not oneMore:
            print("One more button not found")
            return False

        pag.moveTo(oneMore.left + 10, oneMore.top + 10, duration=random.uniform(0.05, 0.1))
        pag.click()
        pag.typewrite(["enter", "enter"])
        pag.moveRel(random.randint(0, 50), random.randint(50, 100), duration=random.uniform(0.05, 0.1))
        return True


def locate_ui():
    """Locate cubing UI"""
    cube_ui = pag.locateOnScreen(res)
    return cube_ui.left, cube_ui.top


def roll(coor):
    basel, baset = coor
    while True:
        sleep(1.3)
        med_sleep()

        strn, dex, inte, luk, allS, hp, att, matt = 0, 0, 0, 0, 0, 0,0 ,0

        strn += 6 * len(list(pag.locateAllOnScreen('img/str6.png', region=(basel, baset, 670, 385),
                                                            confidence="0.97", grayscale=True)))
        strn += 3 * len(list(pag.locateAllOnScreen('img/str3.png', region=(basel, baset, 670, 385),
                                                            confidence="0.97", grayscale=True)))
        dex += 6 * len(list(pag.locateAllOnScreen('img/dex6.png', region=(basel, baset, 670, 385),
                                                        confidence="0.97", grayscale=True)))
        dex += 3 * len(list(pag.locateAllOnScreen('img/dex3.png', region=(basel, baset, 670, 385),
                                                        confidence="0.97", grayscale=True)))
        inte += 6 * len(list(pag.locateAllOnScreen('img/int6.png', region=(basel, baset, 670, 385),
                                                            confidence="0.97", grayscale=True)))
        inte += 3 * len(list(pag.locateAllOnScreen('img/int3.png', region=(basel, baset, 670, 385),
                                                            confidence="0.97", grayscale=True)))
        luk += 6 * len(list(pag.locateAllOnScreen('img/luk6.png', region=(basel, baset, 670, 385),
                                                        confidence="0.97", grayscale=True)))
        luk += 3 * len(list(pag.locateAllOnScreen('img/luk3.png', region=(basel, baset, 670, 385),
                                                        confidence="0.97", grayscale=True)))
        allS += 6 * len(list(pag.locateAllOnScreen('img/all6.png', region=(basel, baset, 670, 385),
                                                            confidence="0.97", grayscale=True)))
        allS += 3 * len(list(pag.locateAllOnScreen('img/all3.png', region=(basel, baset, 670, 385),
                                                            confidence="0.97", grayscale=True)))

        print("STR: %6d%% DEX:%6d%% INT:%6d%% LUK: %6d%% All Stat: %1d%% " % (strn, dex, inte, luk, allS))

        if checkResults(strn, dex, inte, luk, allS):
            print("done")
            okbutc = pag.locateOnScreen(okbut, region=(basel, baset, 670, 385))
            pd.click(okbutc.left+5, okbutc.top+5)
            break
        
        if not oneMoreTime(basel, baset):
            print("One more time button not found, are you out of sus cubes?")
            return
    print("all done")


def checkResults(strn, dex, inte, luk, allS):
    if sys.argv[1] == "a":
        if (strn + allS) >= goal or (dex + allS) >= goal or (inte + allS) >= goal or (luk + allS) >= goal or allS >= goal:
            return True
    elif sys.argv[1] == "str":
        if (strn + allS) >= goal:
            return True
    elif sys.argv[1] == "int":
        print("check")
        if (inte + allS) >= goal:
            return True
    elif sys.argv[1] == "luk":
        if (luk + allS) >= goal:
            return True
    elif sys.argv[1] == "dex":
        if (dex + allS) >= goal:
            return True

# Start
random.seed(9489012)
# USAGE: general.py (stat) (value)
# Enter "a" for stat for any stats
# Enter "str" for Strength
# Enter "int" for Intelligence
# Enter "luk" for Luck
# Enter "dex" for Dexterity
goal = int(sys.argv[2])
print("Rolling for " + sys.argv[1] + " " + str(goal) +"%")
roll(locate_ui())