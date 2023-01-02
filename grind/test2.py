from keyboard import press, release, record, play
import random
from time import time, sleep
import sys

# Open file
ofile = open("inputs.txt", "r")

sleep(2)

print("Playing...")
while 1:
    for a in ofile.readline()[1:-1]:
        play(a)