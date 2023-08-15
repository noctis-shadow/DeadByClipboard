# -*- coding: utf-8 -*-
from sys             import exit as shutdown
from keyboard        import write
from win32gui        import GetWindowText, GetForegroundWindow
from pyperclip       import paste
from pynput.keyboard import Key, HotKey, Listener


def on_activate():
    try:
        if "DeadByDaylight" in GetWindowText(GetForegroundWindow()):
            write(paste())
    except:
        ...

hotkey = HotKey(HotKey.parse('<ctrl>+v'), on_activate)

if __name__ == "__main__":
    with Listener(
        on_press   = lambda key: hotkey.press(listener.canonical(key)) if key != Key.f8 else shutdown(0),
        on_release = lambda key: hotkey.release(listener.canonical(key))
    ) as listener:
        listener.join()
