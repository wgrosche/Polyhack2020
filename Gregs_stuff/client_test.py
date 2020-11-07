import asyncio
import websockets



async def sensor():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            value = 'Sensor_name,1'
            await websocket.send(value)


asyncio.get_event_loop().run_until_complete(sensor())
