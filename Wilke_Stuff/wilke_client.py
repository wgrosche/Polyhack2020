# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:03:07 2020

@author: wilke
"""
import asyncio
import pathlib
import ssl
import websockets

ws = connect("ws://localhost:9000")
cid = ws.recv()
print("Connection established with ID {}".format(cid))
while True:
    try:
        result = ws.recv()
        print("Received: {}".format(result))
    except KeyboardInterrupt:
        ws.close()
        print("Connection closed")
        exit(0)
        


async def chat():
    async with websockets.connect(
            'wss://localhost:8765', ssl=None) as websocket:
        cid = websocket.recv()
        while(True):
            msg = input("Enter message to server (type 'q' to exit):")
            if msg == "q":
            	break;
            await websocket.send(msg)

            msg = await websocket.recv()
            print(f"From Server: {msg}")

asyncio.get_event_loop().run_until_complete(chat())