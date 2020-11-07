import asyncio
import websockets



async def actuator():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input('Input Actuator name: ')
        type = input('Actuator type: ')
        await websocket.send(1,name,type)
        while True:
            value = '0,Sensor_name,1'
            #maybe i could do a measurement here
            # this could for example be done by connecting to another server
            # that simulates movement in the city
            await websocket.send(value)


asyncio.get_event_loop().run_until_complete(sensor())
