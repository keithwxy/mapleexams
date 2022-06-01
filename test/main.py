from time import sleep
from game import Game
import interception
import pyautogui as pag
import pydirectinput as pdi
import random
#from character import Character


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

# Init
random.seed(98039704)
sleep(2)
g = Game()

# Main
while True:
    # Pre rotation checks
    # Check if rune exists, if exists, solve
    if g.locate_rune():
        press("n")
        arrow_directions = g.solve_rune()
        if arrow_directions:
            for i in sorted(arrow_directions):
                print(arrow_directions[i])
                press(arrow_directions[i])
                med_sleep()
        else:
            print("Rune not found / Error in solving rune.")
    break
    # Rotation here