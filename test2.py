# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:45:00 2020

@author: wilke
"""

#!/usr/bin/env python

import asyncio
import pathlib
import ssl
import websockets

async def chat():
    async with websockets.connect(
            'wss://localhost:8765', ssl=None) as websocket:
        while(True):
            msg = input("Enter message to server (type 'q' to exit):")
            if msg == "q":
            	break;
            await websocket.send(msg)

            msg = await websocket.recv()
            print(f"From Server: {msg}")

asyncio.get_event_loop().run_until_complete(chat())