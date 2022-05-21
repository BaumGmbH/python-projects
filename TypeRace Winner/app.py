from time import sleep
from tkinter import Tk

from pyautogui import write

from pynput import keyboard
from pynput.keyboard import Key


r = Tk()
listener = None

clipboard_new = ""

def write_text(key):
    if key == Key.pause:
        write(clipboard_new, interval=0.03)
        listener.stop()

while True:

    r.withdraw()
    clipboard = r.clipboard_get()
    clipboard_new = clipboard

    while clipboard == clipboard_new:
        r.withdraw()
        clipboard_new = r.clipboard_get()
        sleep(0.5)

    with keyboard.Listener(on_press=write_text) as l:
        listener = l
        listener.join()

    



