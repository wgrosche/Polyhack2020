# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:39:21 2020

@author: wilke
"""

#!/usr/bin/env python

import websockets
from websockets import WebSocketServerProtocol
import asyncio
import logging


class Server:
    def __init__(self):
        self.clients = set()
        self.loop = asyncio.get_event_loop()
        self.logger = _create_logger()
        self._client_timeout = 5
        self._wake_up_task = None

    def listen(self, host='localhost', port=1299):
        self.logger.info("listening on {}:{}".format(host, port))
        ws_server = websockets.serve(self.connect_client, host, port)

        self.loop.run_until_complete(ws_server)
        self._wake_up_task = asyncio.ensure_future(_wake_up())

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.logger.debug('caught keyboard interrupt')
            self.exit()

    async def connect_client(self, client: WebSocketServerProtocol, path):
        self.clients.add(client)
        self.logger.info('new client connected from {}:{}'.format(*client.remote_address))
        keep_alive_task = asyncio.ensure_future(self.keep_alive(client))

        try:
            await self.handle_messages(client)
        except websockets.ConnectionClosed:
            keep_alive_task.cancel()
            await self.disconnect_client(client)

    async def handle_messages(self, client):
        while True:
            message = await client.recv()
            self.logger.info('recieved message from {}:{}: {}'.format(*client.remote_address, message))
            await asyncio.wait([client.send(message) for client in self.clients])

    async def disconnect_client(self, client):
        await client.close()
        self.clients.remove(client)
        self.logger.info('client {}:{} disconnected'.format(*client.remote_address))

    async def keep_alive(self, client: WebSocketServerProtocol):
        while True:
            await asyncio.sleep(self._client_timeout)
            try:
                self.logger.info('pinging {}:{}'.format(*client.remote_address))
                await asyncio.wait_for(client.ping(), self._client_timeout)
            except asyncio.TimeoutError:
                self.logger.info('client {}:{} timed out'.format(*client.remote_address))
                await self.disconnect_client(client)

    def exit(self):
        self.logger.info("exiting")
        self._wake_up_task.cancel()
        try:
            self.loop.run_until_complete(self._wake_up_task)
        except asyncio.CancelledError:
            self.loop.close()


def _create_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("chat.server")
    logger.setLevel(logging.INFO)
    ws_logger = logging.getLogger('websockets.server')
    ws_logger.setLevel(logging.ERROR)
    ws_logger.addHandler(logging.StreamHandler())
    return logger


async def _wake_up():
    while True:
        await asyncio.sleep(1)


def main():
    server = Server()
    server.listen()


if __name__ == "__main__":
    main()