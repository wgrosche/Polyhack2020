import asyncio
import websockets
import json


async def actuator():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input('Input Actuator name: ')
        type = input('Actuator type: ')
        mes = '2' + ',' + name + ',' + type
        await websocket.send(mes)

        while True:
            while websocket:
                print("Test")
                async for message in websocket:
                    state = json.loads(message)
            state = state[name]
            print(state)

asyncio.get_event_loop().run_until_complete(actuator())
