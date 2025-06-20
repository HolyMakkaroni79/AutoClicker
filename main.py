import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOOGLE_KEY = KeyCode(char="ü")
sleep_time = 0.01
left_click = True

clicking = False
mouse = Controller()

def clicker():
    while True:
        if  clicking is True and left_click is True:
            mouse.click(Button.left, 1)
        elif clicking is True and left_click is False:
            mouse.click(Button.right, 1)
        time.sleep(sleep_time)

def toogle_event(key):
    if key == TOOGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toogle_event) as Listener:
    Listener.join()
