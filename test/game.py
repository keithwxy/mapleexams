import face_recognition as fr
import pygetwindow
import pyautogui as pag
import pydirectinput as pdi
from PIL import Image, ImageEnhance, ImageOps
from time import sleep
import psutil
import random


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


class Game:
    def __init__(self):
        random.seed(98039704)
        self.uparr = "arrow/up.png"
        self.dwarr = "arrow/dw.png"
        self.ltarr = "arrow/lt.png"
        self.rtarr = "arrow/rt.png"
        self.challenge = "arrow/challenge.png"
        # Locate game window
        window_coords = pag.locateOnScreen("img/game_window.png", confidence=0.98)
        self.winl = window_coords.left
        self.wint = window_coords.top
        # Locate minimap


    def convert_image(self):
        # Convert to RGB
        img = Image.open(self.challenge).convert('RGB')
        # Invert image
        img = ImageOps.invert(img)
        # Max brightness
        enh = ImageEnhance.Brightness(img)
        img = enh.enhance(2.5)
        img.save(self.challenge)
        img.close()
        # Change to black and white
        img = Image.open(self.challenge)
        img = img.convert("L")
        img = img.point( lambda p: 255 if p > 235 else 0)
        img = img.convert("1")
        img.save(self.challenge)
        img.close()

    def solve_rune(self):
        """Solves rune"""
        answers = {}
        # Retrieve screenshot of rune area
        pag.screenshot("arrow/challenge.png", region=(self.winl+385, self.wint+147, 580, 230))
        # Convert to binary
        self.convert_image()
        # Locate arrows
        chalimg = Image.open(self.challenge)
        chalimg.show()
        # Check if photo viewer is open, if not open it
        if not pag.locateOnScreen("img/photo_viewer.png", confidence=0.99, region=(0, 0, 500, 400)):
            # Locate window
            viewer_cords = pag.locateOnScreen("img/photo_color.png", confidence=0.9)
            pag.click(viewer_cords.left+5, viewer_cords.top+5)
        uplist = pag.locateAllOnScreen(self.uparr, confidence=0.80, region=(0, 0, 1300, 800))
        if uplist:
            for i in uplist:
                answers[i.left] = "up" # 72 
        dwlist = pag.locateAllOnScreen(self.dwarr, confidence=0.80, region=(0, 0, 1300, 800))
        if dwlist:
            for i in dwlist:
                answers[i.left] = "down" # 80
        ltlist = pag.locateAllOnScreen(self.ltarr, confidence=0.80, region=(0, 0, 1300, 800))
        if ltlist:
            for i in ltlist:
                answers[i.left] = "left" # 75
        rtlist = pag.locateAllOnScreen(self.rtarr, confidence=0.80, region=(0, 0, 1300, 800))
        if rtlist:
            for i in rtlist:
                answers[i.left] = "right" # 77
        # Close image
        for proc in psutil.process_iter():
            if proc.name() == "Microsoft.Photos.exe":
                proc.kill()
        # Clean dictionary
        prevx = 0
        for i in sorted(answers.keys()):
            if i - prevx < 20:
                answers.pop(i)
            prevx = i
        print(answers)
        print(len(answers))
        if len(answers) != 4:
            return None
        # Click back into game
        pag.click(self.winl+5, self.wint+5)
        
        return answers

    def locate_char(self):
        charloc = pag.locateOnScreen("img/player.png", region=(self.winl+10, self.wint, 400, 200), confidence=0.95)
        return charloc
    
    def locate_rune(self):
        runeloc = pag.locateOnScreen("img/rune.png", region=(self.winl+10, self.wint, 400, 200), confidence=0.90)
        if runeloc:
            self.goto_loc(runeloc.left, runeloc.top)
            return True
        return False
    
    def goto_loc(self, locx, locy):
        """Bring player to designated location"""
        while True:
            player_location = self.locate_char()
            if player_location is None:
                print("Attempting to locate player")
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
                    pdi.keyDown("down")
                    small_sleep()
                    press("space")
                    small_sleep()
                    pdi.keyUp("down")
                # Player is below target y-position.
                else:
                    if y1 - y2 > 20:
                        press("3") # Rope Lift
                    else:
                        press("up")
                        press("up")
                # Delay for player falling down or jumping up.
                sleep(1)
            else:
                # Player is to the left of target x-position.
                if x1 < x2:
                    pdi.keyDown("right")
                # Player is to the right of target x-position.
                else:
                    pdi.keyDown("left")
                if abs(x2 - x1) > 30:
                    print("Flash jump")
                    press("space")
                    press("space")
        

# enhancer2 = ImageEnhance.Brightness(img)
# img = enhancer2.enhance(0.1)

# enhancer = ImageEnhance.Contrast(img)
# img = enhancer.enhance(16)

# img.save("testgray.png")


#pyautogui.screenshot(ss_path, region=(450, 180, 360, 170))

# x1, y1, w, h = pyautogui.locateOnScreen(arcs, region=(400, 120, 400, 300), grayscale=True, confidence=0.65)
# x2, y2, w, h = pyautogui.locateOnScreen(arce, region=(400, 120, 400, 300), grayscale=True, confidence=0.65)

# pyautogui.screenshot(ss_path, region=(x1, y1, 100, 100))
# pyautogui.screenshot(ss_path2, region=(x2, y2, 100, 100))

#abc = pyautogui.locateAllOnScreen(chal, grayscale=True, confidence=0.55, region=(400, 120, 400, 200))

#print(list(abc))
#print(bbc)