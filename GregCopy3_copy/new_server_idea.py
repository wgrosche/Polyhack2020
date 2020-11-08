# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:53:07 2020

@author: wilke
"""

import websockets
from websockets import WebSocketServerProtocol
import asyncio
import logging

import ruleset as rules
import config
import importlib
import json
global server
server = rules.Server()


class Server:
    def __init__(self):
        self.clients = set()
        self.loop = asyncio.get_event_loop()
        self.logger = _create_logger()
        self._client_timeout = 5
        self._wake_up_task = None

    def listen(self, host='localhost', port=8765):
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

    async def handle_messages(self, client, message):
        while True:
            self.message_processor(await client.recv())
            self.status_update()
            message = self.status_string
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
                
    def message_processor(self, data):
        data = data.split(',') # First entry: Sensor name, Second Entry: Value
        if data[0]=='0':
            # now i want to update the sensor:
            server.devices[data[1]].value = float(data[2])
        elif data[0]=='1':
            #eval(data[1]) = config.eval(data[2])(name = data[1])
            #class_ = getattr(rules , data[2])
            #exec("%s = %d" % (data[1],class_()))
            #exec("%s = %d" % (data[1],rules.eval(data[2])(name = data[1])))
            server.ServerAddDevices(data)
            importlib.reload(config)
            self.sensors.append(data[1])
            print(self.sensors)
        elif data[0]=='2':
            #eval(data[1]) = config.eval(data[2])(name = data[1])
            #class_ = getattr(rules , data[2])
            #exec("%s = %d" % (data[1],class_()))
            #exec("%s = %d" % (data[1],rules.eval(data[2])(name = data[1])))

            server.status[data[1]] = False
            server.ServerAddDevices(data)
            importlib.reload(config)
            self.actuators.append(data[1])
            print(self.actuators)
            
    def status_update(self):
        importlib.reload(config)
        config.updates(server)
        self.status = server.status
        self.status_string = json.dumps(self.status)


    def exit(self):
        self.logger.info("exiting")
        self._wake_up_task.cancel()
        try:
            self.loop.run_until_complete(self._wake_up_task)
        except asyncio.CancelledError:
            self.loop.close()
            
    async def rule_engine(self, websocket, path):

        #config.init_sensors()
        self.sensors = []
        self.actuators = []
        
        while True:
            for i in range(20):
                try:
                    data = await websocket.recv()
                    data = data.split(',') # First entry: Sensor name, Second Entry: Value
    
                    if data[0]=='0':
                        # now i want to update the sensor:
                        server.devices[data[1]].value = float(data[2])
                    elif data[0]=='1':
                        #eval(data[1]) = config.eval(data[2])(name = data[1])
                        #class_ = getattr(rules , data[2])
                        #exec("%s = %d" % (data[1],class_()))
                        #exec("%s = %d" % (data[1],rules.eval(data[2])(name = data[1])))
    
                        server.ServerAddDevices(data)
    
                        importlib.reload(config)
                        self.sensors.append(data[1])
                        print(self.sensors)
                    elif data[0]=='2':
                        #eval(data[1]) = config.eval(data[2])(name = data[1])
                        #class_ = getattr(rules , data[2])
                        #exec("%s = %d" % (data[1],class_()))
                        #exec("%s = %d" % (data[1],rules.eval(data[2])(name = data[1])))
    
                        server.status[data[1]] = False
                        server.ServerAddDevices(data)
    
                        importlib.reload(config)
                        self.actuators.append(data[1])
                        print(self.actuators)
    
                    await asyncio.sleep(0.2)
    
                except websockets.ConnectionClosed:
                    #print(f"Terminated")
                    break
    
            #logic phase
            importlib.reload(config)
            config.updates(server)
            # websocket.connections.itervalues():
                
            # for actuator in actuators:
            #     await websocket.send(server.status[actuator])
            status_string = json.dumps(server.status) #data serialized
            for client in self.clients:
                await self.handle_messages(client, status_string)
            await asyncio.sleep(2)



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