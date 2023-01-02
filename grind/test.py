from keyboard import press, release, record, play
import random
from time import time, sleep
import sys

# Open file
#ofile = open("inputs.txt", "a+")

sleep(2)

print("Recording...")
a = record(until="ins")
play(a, speed_factor=0.98)