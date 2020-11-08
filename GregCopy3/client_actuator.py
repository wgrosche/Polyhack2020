import asyncio
import websockets


global status, actuator_name, actuator_type
status = 0

async def actuator_init():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        actuator_name = input('Input Actuator name: ')
        actuator_type = input('Actuator type: ')
        mes = '2' + ',' + actuator_name + ',' + actuator_type
        await websocket.send(mes)
        while True:
            status_all = await websocket.recv()
            status = status_all["actuator_name"]
            status_update = '0' + ',' + status
            await websocket.send(status_update)
            await asyncio.sleep(1)

            

asyncio.get_event_loop().run_until_complete(actuator_init())
asyncio.get_event_loop().run_forever()