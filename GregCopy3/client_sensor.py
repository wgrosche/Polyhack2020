import asyncio
import websockets
import random
import json


async def sensor():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input('Input Sensor name: ')
        #name = 'CatProximity'
        type = input('Sensor type: ')
        #type = 'ProximitySensor'
        #value = input('Measurement: ')
        value = '0.8'
        value = float(value)
        mes = '1' + ',' + name + ',' + type
        await websocket.send(mes)
        while True:
            print(value)
            # (stating that this is sensor data, name , value)
            data = '0,' + name + ',' + str(value)
            if type == "ProximitySensor":
                value = random.random()
            else:
                value = random.getrandbits(1)
            #maybe i could do a measurement here
            # this could for example be done by connecting to another server
            # that simulates movement in the city
            await websocket.send(data)
            await asyncio.sleep(0.7)
            #message = await websocket.recv()
            #print(json.loads(message))


asyncio.get_event_loop().run_until_complete(sensor())
