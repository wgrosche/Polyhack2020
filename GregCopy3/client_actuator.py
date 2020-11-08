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
            print("Test")
            message = await websocket.recv()
            print(json.loads(message))

            state = json.loads(message)
            try:
                state = state[name]
            except KeyError:
                pass
            print(state)


asyncio.get_event_loop().run_until_complete(actuator())
