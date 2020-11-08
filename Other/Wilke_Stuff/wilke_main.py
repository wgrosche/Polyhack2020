# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:37:20 2020

@author: wilke
"""

import websockets
import asyncio
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

"""
Server:
    Pulls status from devices at regular intervals
    Calculates response based on the ruleset
    Pushes update to corresponding device
    
Device:
    Attribute updated based on server push
"""

"""

"""
# import ruleset
# import config
        

# class Server():
#     def __init__(config, ruleset):
#         start_server = websockets.serve(time, "127.0.0.1", 5678)
#         asyncio.get_event_loop().run_until_complete(start_server)
#         asyncio.get_event_loop().run_forever()
#         pass
#     async def pull(input_data, device):
#         for sensor in sensors:
#             sensor.update()
        
#     async def push():
#         for actuator in actuators:
#             actuator.update()


#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

# import asyncio
# import pathlib
# import ssl
# import websockets

# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")

#     greeting = f"Hello {name}!"

#     await websocket.send(greeting)
#     print(f"> {greeting}")

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)

# start_server = websockets.serve(
#     hello, "localhost", 8765, ssl=ssl_context
# )

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS


# Source: https://stackoverflow.com/questions/29951718/autobahn-sending-user-specific-and-broadcast-messages-from-external-application
class BroadcastServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.register(self)

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))

    def onMessage(self, payload, isBinary):
        if not isBinary:
            if (msg := payload.decode("utf-8")).startswith("@a"):
                self.factory.broadcast("Got message: " + msg)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = []

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        print("broadcasting message '{}' to {} clients ...".format(msg, len(self.clients)))
        for c in self.clients:
            c.sendMessage(msg.encode('utf-8'))


if __name__ == "__main__":
    ServerFactory = BroadcastServerFactory
    factory = ServerFactory("ws://localhost:9000")

    factory.protocol = BroadcastServerProtocol
    listenWS(factory)

    webdir = File(".")
    web = Site(webdir)
    reactor.listenTCP(8080, web)

    reactor.run()
    
    

import uuid

# ...

class BroadcastServerFactory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = {}

    def register(self, client):
        registered = [self.clients[i] for i in list(self.clients.keys())]
        ids = list(self.clients.keys())
        if client not in registered:
            while (cid := str(uuid.uuid4())) in ids:
                pass

            print("registered client {} with id {}".format(client.peer, cid))
            client.sendMessage(cid.encode())
            self.clients[cid] = client

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        print("broadcasting message '{}' to {} clients ...".format(msg, len(self.clients)))
        for cid in self.clients:
            self.clients[cid].sendMessage(msg.encode('utf-8'))


