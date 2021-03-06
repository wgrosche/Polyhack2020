import asyncio
import websockets



async def actuator():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        act_name = input('Input Actuator name: ')
        act_type = input('Actuator type: ')
        mes = '2' + ' ' + act_name + ' ' + act_type
        await websocket.send(mes)


asyncio.get_event_loop().run_until_complete(actuator())
asyncio.get_event_loop().run_forever()
