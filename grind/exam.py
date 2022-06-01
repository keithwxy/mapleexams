import pydirectinput as pdi
import random
from time import time, sleep
import sys


if len(sys.argv) != 3:
    print("Usage: python <script> <class> <rotations>")
    sys.exit()

rots = sys.argv[2]
inputs = []

for i in range(1, int(rots)+1):
    print("Loading rot %d" % i)
    f = open(sys.argv[1] + str(i) +".txt", "r")
    inputs.append([])
    for x in f.readlines():
        a = x.split(" ")
        ats = float(a[0])
        key = a[1].strip("Key.")
        key = key.strip("'")
        if key == "nd":
            key = "end"
        if key == "spac":
            key = "space"
        action = a[2]
        temparr = [ats, key, action]
        inputs[i-1].append(temparr)
    f.close()

print(inputs)

ats = 0.00
cts = 0.00
tempcts = 0.00
key = ""
action = ""
random.seed(86879877)
sleep(1)
while True:
    rotation = random.randint(0, int(rots)-1)
    print("Rotation %d chosen" % rotation)
    bts = time()
    for x in inputs[rotation]:
        #print("Rotation %d chosen" % x+1)
        #print(z)
        ats = x[0]
        key = x[1]
        action = x[2]
        cts = tempcts
        while cts < ats:
            cts = time() - bts
        cts = ats
        if "PRESS" in action:
            print("PRESS", key)
            while not pdi.keyDown(key):
                continue
            tempcts = time() - bts - cts
            continue
        else:
            print("RELEASE", key)
            while not pdi.keyUp(key):
                continue
            tempcts = time() - bts - cts
            continue
    # Rotation complete, reset bts