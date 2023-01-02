import keyboard
import sys
import os
import pickle

if len(sys.argv) != 3:
    print("Usage: python study.py <class> <map>")

CLASS = sys.argv[1]
FOLDER_NAME = os.getcwd() + "/" + sys.argv[1] + sys.argv[2]
COUNT = 0

# Record keys
keys = keyboard.record(until='esc')

# Save object to file
if not os.path.exists(FOLDER_NAME+"/"):
    os.mkdir(FOLDER_NAME)
for files in os.listdir(FOLDER_NAME):
    if os.path.isfile(os.path.join(FOLDER_NAME, files)):
        COUNT += 1

FILE_NAME = FOLDER_NAME+"/"+CLASS+str(COUNT)
with open(FILE_NAME, "wb") as fp:
    pickle.dump(keys, fp)
