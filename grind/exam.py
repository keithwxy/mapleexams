import keyboard
import sys
import os
import pickle
import random
import time
from threading import Thread


if len(sys.argv) != 3:
    print("Usage: python exam.py <class> <map>")

time.sleep(1.5)
CLASS = sys.argv[1]
FOLDER_NAME = os.getcwd() + "/" + sys.argv[1] + sys.argv[2]
ROTATIONS = []
BASE_TIME = 0
CURR_TIME = 0
END_TIME = 0

keys2 = []
for files in os.listdir(FOLDER_NAME):
    if os.path.isfile(os.path.join(FOLDER_NAME, files)):
        with open(os.path.join(FOLDER_NAME, files), "rb") as fp:
            keys2 = pickle.load(fp)
            keys2.pop()
            ROTATIONS.append(keys2)

for i in ROTATIONS:
    for x in range(1, len(i)):
        i[x].time = i[x].time - i[0].time
    i[0].time = 0

def run_time():
    BASE_TIME = time()
    while CURR_TIME <= END_TIME:
        CURR_TIME = time() - BASE_TIME

def play_keys():
    while True:
        rand = random.randint(0, len(ROTATIONS)-1)
        print("Playing rotation %d" % rand)
        END_TIME = ROTATIONS[rand][len(ROTATIONS[rand]-1)].time
        timer_thread.start()
        for rot in ROTATIONS[rand]:

    keyboard.start_recording()
    keyboard.stop_recording()
    keyboard.play(ROTATIONS[rand], speed_factor=1)

timer_thread = Thread(target=run_time)
press_thread = Thread(target=play_keys)


quit()
while True:
    rand = random.randint(0, len(ROTATIONS)-1)
    print("Playing rotation %d" % rand)
    keyboard.start_recording()
    keyboard.stop_recording()
    keyboard.play(ROTATIONS[rand], speed_factor=1)
