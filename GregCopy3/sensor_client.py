import asyncio
import websockets
import random

"""
Sensor Client for the ASUS PolyHack Challenge:
    Can take sensor types as per the ruleset file. These are ProximitySensor(Continuous), MotionSensor(Discrete),NoiseDetector(Discrete)
"""
async def sensor():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Read in the sensor name
        act_name = input('Input Sensor name: ')
        # Read in the sensor type
        act_type = input('Sensor type: ')
        msg = '1' + ',' + act_name + ',' + act_type
        await websocket.send(msg)
        while True:
            # for simulation purposes only: this generates random values for the sensor
            if type == "ProximitySensor":
                act_value = random.random()
            else:
                act_value = random.getrandbits(1)
            print(act_value)
            # (stating that this is sensor data, name , value)
            data = '0,' + act_name + ',' + str(act_value)
            # sends new status to the server
            await websocket.send(data)
            await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(sensor())
