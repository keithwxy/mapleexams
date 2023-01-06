import keyboard
import sys
import os
import pickle
import random
import time


if len(sys.argv) != 3:
    print("Usage: python exam.py <class> <map>")

time.sleep(1)
CLASS = sys.argv[1]
FOLDER_NAME = os.getcwd() + "/" + sys.argv[1] + sys.argv[2]
ROTATIONS = []

keys2 = []
for files in os.listdir(FOLDER_NAME):
    if os.path.isfile(os.path.join(FOLDER_NAME, files)):
        with open(os.path.join(FOLDER_NAME, files), "rb") as fp:
            keys2 = pickle.load(fp)
            keys2.pop()
            ROTATIONS.append(keys2)

print(ROTATIONS)
while True:
    rand = random.randint(0, len(ROTATIONS)-1)
    print("Playing rotation %d" % rand)
    keyboard.start_recording()
    keyboard.stop_recording()
    keyboard.play(ROTATIONS[rand], speed_factor=1)
