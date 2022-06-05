from pynput.keyboard import Key, Listener
import time
import sys


def on_press(key):
    # Quit
    ts = time.time() -t
    if key == Key.esc:
        f.close()
        return False
    if key in pressed:
        return
    pressed.append(key)
    temp = str(ts) + " " + str(key) + " " + "PRESS\n"
    f.write(temp)
    #print("%f %s PRESS", ts, key)
 

def on_release(key):
    ts = time.time() -t
    # Quit
    if key == Key.esc:
        f.close()
        return False
    pressed.remove(key)
    temp = str(ts) + " " +str(key) + " " + "RELEASE\n"
    f.write(temp)
    #print("%f %s RELEASE", ts, key)

pressed = []
time.sleep(1)
print("Start")
temps = sys.argv[1] + sys.argv[2] + ".txt"
f = open(temps, "w")
t = time.time()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()