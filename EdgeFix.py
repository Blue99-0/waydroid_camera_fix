#!/usr/bin/env python3

import pyautogui as py
import mouse
import time
import asyncio

py.FAILSAFE = False

async def MouseCorner():
    time.sleep(0.1)

    mousepos = py.position()
    if mousepos.x == 1365:
        py.moveTo(1, mousepos.y)

    if mousepos.x <= 0:
        py.moveTo(1366,mousepos.y)
            

    
while True:
    time.sleep(0.1)
    asyncio.run(MouseCorner())
