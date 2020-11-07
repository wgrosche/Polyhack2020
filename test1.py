# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:44:53 2020

@author: wilke
"""

#!/usr/bin/env python

import asyncio
import pathlib
import ssl
import websockets

async def chat(websocket, path):
    while(True):
        msg = await websocket.recv()
        print(f"From Client: {msg}")

        msg = input("Enter message to client(type 'q' to exit): ")
        if msg == "q":
        	break;
        await websocket.send(msg)

start_server = websockets.serve(
	chat, 'localhost', 8765, ssl=None)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
