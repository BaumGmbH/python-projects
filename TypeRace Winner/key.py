from pynput import keyboard
from pynput.keyboard import Key

l = None

def press(k):
    print(k)
    if k == Key.enter:
        l.stop()

with keyboard.Listener(on_press=press) as listener:
        l = listener
        listener.join()


print("end")
