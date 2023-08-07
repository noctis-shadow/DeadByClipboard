# -*- coding: utf-8 -*-
from sys       import exit as shutdown
from pynput    import keyboard
from keyboard  import write
from win32gui  import GetWindowText, GetForegroundWindow
from pyperclip import paste


def on_activate():
    try:
        name = GetWindowText(GetForegroundWindow())

        if "DeadByDaylight" in name:
            write(paste())
    except:
        ...

def for_canonical(key_event):
    try:
        return lambda key: key_event(listener.canonical(key)) if key != keyboard.Key.f8 else shutdown(0)
    except:
        ...

hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+v'), on_activate)

if __name__ == "__main__":
    with keyboard.Listener(
        on_press   = for_canonical(hotkey.press),
        on_release = for_canonical(hotkey.release)
    ) as listener:
        listener.join()