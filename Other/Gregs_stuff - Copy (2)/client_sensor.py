import asyncio
import websockets



async def sensor():
    uri = "ws://localhost:8765"
    uri_city = "ws://localhost:8766"

    #initialization
    async with websockets.connect(uri) as websocket:
        name = input('Input Sensor name: ')
        type = input('Sensor type: ')
        value = input('Measurement: ')
        mes = '1' + ',' + name + ',' + type
        await websocket.send(mes)

    #measurements
    async with websockets.connect(uri_city) as websocket:
        mes = name + ',' type
        await websocket.send(mes)

    # communication
    async with websockets.connect(uri) as websocket:
        while True:
            # (stating that this is sensor data, name , value)
            data = '0,' + name + ',' + value
            #maybe i could do a measurement here
            # this could for example be done by connecting to another server
            # that simulates movement in the city
            await websocket.send(data)
            await asyncio.sleep(0.3)


asyncio.get_event_loop().run_until_complete(sensor())
