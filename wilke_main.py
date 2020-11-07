# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:37:20 2020

@author: wilke
"""

import websockets as wbs
import asyncio as aio
import numpy as np
import pandas as pd
import requests as rq
import ssl

# Asus PolyHack Challenge


## Ruleset
# information provided by the end user to define the
# actions taken in response certain stimuli
# ruleset = ...

# ## Device Type
# # device type defines the number of input and output arguments
# # it can take based on the ruleset. sensors can read signals
# # from the environment and output information to the central api server
# # actuators can take input information from the central server
# # and output to the environment. 
# dev_type = ...


class device():
    async def _init_(dev_type):
        self.ruleset = dev_type.ruleset
        self.
        pass
    async def server_pull(input_data):
        self.output_data_pull = self.ruleset(input_data)
        return self.output_data_pull
        
    async def server_push(input_data):
        self.output_data_push = self.ruleset(input_data)
        return self.output_data_push
        
class dev_type():
    def _init_():
        

class server():


# def device_request(dev_type, input_data):
#     global ruleset
    
# def 

#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import pathlib
import ssl
import websockets

vd def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(
    hello, "localhost", 8765, ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()