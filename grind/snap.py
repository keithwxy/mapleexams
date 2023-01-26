import pyautogui as pag
from time import sleep
import pyautogui as pag
import pydirectinput as pdi
import random


def small_sleep():
    sleep(random.randint(1, 3)/100)


def press(key):
    pdi.keyDown(key)
    small_sleep()
    pdi.keyUp(key)


def hold(key, duration):
    pdi.keyDown(key)
    sleep(duration)
    pdi.keyUp(key)

def fj():
    pdi.press("space")
    pdi.press("space")

def downjump():
    pdi.keyDown("down")
    small_sleep()
    press("space")
    small_sleep()
    pdi.keyUp("down")

def upjump():
    press("space")
    small_sleep()
    pdi.keyDown("up")
    press("space")
    pdi.keyUp("up")

def uptele():
    pdi.keyDown("up")
    press("shift")
    pdi.keyUp("up")

def locate_map():
    return pag.locateOnScreen("img/game_window.png", confidence=0.95)


def locate_char(anchorx, anchory):
        charloc = pag.locateOnScreen("img/player.png", region=(anchorx+10, anchory+20, 500, 300), confidence=0.95)
        return charloc


def goto_loc(anchorx, anchory, locx, locy):
        """Bring player to designated location"""
        while True:
            x = 0
            player_location = locate_char(anchorx, anchory)
            if player_location is None:
                print("Attempting to locate player")
                if x >= 0:
                    pdi.keyDown("right")
                    sleep(0.4)
                    pdi.keyUp("right")
                    x = 1
                else: 
                    pdi.keyDown("left")
                    sleep(0.4)
                    pdi.keyUp("left")
                    x = 0
                continue

            print("Moving player...")
            x1, y1 = player_location.left, player_location.top
            x2, y2 = locx, locy

            """
            There are delays between taking a screenshot, processing the image, sending the key press, and game server ping.
            Player should be within 2 pixels of x-destination and 7 pixels of y-destination.
            """
            if abs(x1 - x2) < 2:
                # Player has reached target x-destination, release all held keys.
                print("X Destination reached")
                pdi.keyUp("left")
                pdi.keyUp("right")
                pdi.keyUp("up")
                pdi.keyUp("down")
                if abs(y2 - y1) < 7:
                    # Player has reached target y-destination, release all held keys.
                    print("Y Destination reached")
                    pdi.keyUp("left")
                    pdi.keyUp("right")
                    pdi.keyUp("up")
                    pdi.keyUp("down")
                    break
                # Player is above target y-position.
                elif y1 < y2:
                    downjump()
                # Player is below target y-position.
                else:
                    if y1 - y2 > 20:
                        # Up jump
                        #upjump()
                        # Up tele
                        uptele()
                        # Arcana
                        #downjump()
                    else:
                        # Climb rope
                        #press("up")
                        #press("up")
                        # Teleport
                        #pdi.keyDown("up")
                        #pdi.press("shift")
                        #pdi.keyUp("up")
                        # Up tele
                        uptele()
                        # Arcana
                        #downjump()
                # Delay for player falling down or jumping up.
                sleep(1)
            else:
                # Player is to the left of target x-position.
                if x1 < x2:
                    pdi.keyUp("left")
                    pdi.keyDown("right")
                    # Arcana
                    #downjump()
                # Player is to the right of target x-position.
                else:
                    pdi.keyUp("right")
                    pdi.keyDown("left")
                    # Arcana
                    #downjump()
                if abs(x2 - x1) > 30:
                    # Teleport
                    press("shift")
                    # FJ
                    #press("space")
                    #press("space")
                    # Arcana
                    #downjump()