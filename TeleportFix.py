#!/usr/bin/env python3

import pyautogui as py
import mouse
import time
from pynput.mouse import Listener
import asyncio

og_x = 0
og_y = 0

async def MouseSave():
    def on_click(*args):

        print(args)
        if args[-1]:
            if str(args[-2]) == "Button.right":
               global og_x
               global og_y
               og_x = py.position().x
               og_y = py.position().y

        elif not args[-1]:
          if str(args[-2]) == "Button.right":
                py.moveTo(og_x, og_y)
            

    with Listener(on_click=on_click) as listener:
        listener.join()

while True:
    time.sleep(0.1)
    asyncio.run(MouseSave())
