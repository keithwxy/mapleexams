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

def small_sleep():
    sleep(random.randint(1, 3)/100)


def med_sleep():
    sleep(random.randint(4, 6)/100)


def use_cube():
    """Locate and use cube"""
    cc = pag.locateOnScreen(cube)
    # Double click cube
    pd.click(cc.left+5, cc.top+5)
    small_sleep()
    pd.click(cc.left+5, cc.top+5)


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


def silver_blossom():
    """Scroll all silver blossoms"""
    # Locate inventory
    ic = pag.locateOnScreen(ivimg, confidence="0.9")
    #pag.screenshot("ss.png", region=(ic.left, ic.top, 670, 385))

    # Locate all silver blossoms
    allsilv = pag.locateAllOnScreen(sbimg)
    
    # Use cube
    pd.click(ic.left+40, ic.top+10)
    use_cube()

    # Iterate through
    for i in allsilv:
        pd.click(i.left+3, i.top+3)
        pag.press("enter")
        while True:
            sleep(1.3)
            med_sleep()

            strn, dex, inte, luk, allS, hp, att, matt = 0, 0, 0, 0, 0, 0,0 ,0

            strn += 6 * len(list(pag.locateAllOnScreen('img/str6.png', region=(ic.left, ic.top, 670, 385),
                                                              confidence="0.97", grayscale=True)))
            strn += 3 * len(list(pag.locateAllOnScreen('img/str3.png', region=(ic.left, ic.top, 670, 385),
                                                             confidence="0.97", grayscale=True)))
            dex += 6 * len(list(pag.locateAllOnScreen('img/dex6.png', region=(ic.left, ic.top, 670, 385),
                                                            confidence="0.97", grayscale=True)))
            dex += 3 * len(list(pag.locateAllOnScreen('img/dex3.png', region=(ic.left, ic.top, 670, 385),
                                                            confidence="0.97", grayscale=True)))
            inte += 6 * len(list(pag.locateAllOnScreen('img/int6.png', region=(ic.left, ic.top, 670, 385),
                                                             confidence="0.97", grayscale=True)))
            inte += 3 * len(list(pag.locateAllOnScreen('img/int3.png', region=(ic.left, ic.top, 670, 385),
                                                             confidence="0.97", grayscale=True)))
            luk += 6 * len(list(pag.locateAllOnScreen('img/luk6.png', region=(ic.left, ic.top, 670, 385),
                                                            confidence="0.97", grayscale=True)))
            luk += 3 * len(list(pag.locateAllOnScreen('img/luk3.png', region=(ic.left, ic.top, 670, 385),
                                                            confidence="0.97", grayscale=True)))
            allS += 6 * len(list(pag.locateAllOnScreen('img/all6.png', region=(ic.left, ic.top, 670, 385),
                                                             confidence="0.97", grayscale=True)))
            allS += 3 * len(list(pag.locateAllOnScreen('img/all3.png', region=(ic.left, ic.top, 670, 385),
                                                             confidence="0.97", grayscale=True)))

            print("STR: %6d%% DEX:%6d%% INT:%6d%% LUK: %6d%% All Stat: %1d%% " % (strn, dex, inte, luk, allS))

            if checkResults(strn, dex, inte, luk, allS):
                print("done")
                okbutc = pag.locateOnScreen(okbut, region=(ic.left, ic.top, 670, 385))
                pd.click(okbutc.left+5, okbutc.top+5)
                break
            
            if not oneMoreTime(ic.left, ic.top):
                print("One more time button not found, are you out of sus cubes?")
                return
        
        print("Cubing one more")
        # Cubing for one done
        pd.click(ic.left+40, ic.top+10)
        use_cube()
    print("all done")


def checkResults(strn, dex, inte, luk, allS):
    if (strn + allS) >= 12 or (dex + allS) >= 12 or (inte + allS) >= 12 or (luk + allS) >= 12 or allS >= 12:
        return True


# Start
random.seed(9489012)
silver_blossom()