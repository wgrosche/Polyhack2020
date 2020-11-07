# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:02:53 2020

@author: wilke
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS
import uuid


# Source: https://stackoverflow.com/questions/29951718/autobahn-sending-user-specific-and-broadcast-messages-from-external-application
class BroadcastServerProtocol(WebSocketServerProtocol):
    def onOpen(self):
        self.factory.register(self)

    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))

    def onMessage(self, payload, isBinary):
        if not isBinary:
            payload = payload.decode('utf-8')
            cid = payload[:payload.index(":")]
            msg = payload[payload.index(":")+1:]
            self.factory.broadcast("User {} sent a message: {}".format(cid, msg))

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):
    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = {}

    def register(self, client):
        registered = [self.clients[i] for i in list(self.clients.keys())]
        ids = list(self.clients.keys())
        if client not in registered:
            cid = str(uuid.uuid4())
            while cid in ids:
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


if __name__ == "__main__":
    ServerFactory = BroadcastServerFactory
    factory = ServerFactory("ws://localhost:9000")

    factory.protocol = BroadcastServerProtocol
    listenWS(factory)

    webdir = File(".")
    web = Site(webdir)
    reactor.listenTCP(8080, web)

    reactor.run()