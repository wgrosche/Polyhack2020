import asyncio
import websockets
import random

"""
Sensor Client for the ASUS PolyHack Challenge:
    Can take sensor types as per the ruleset file. These are ProximitySensor(Continuous), MotionSensor(Discrete),NoiseDetector(Discrete)
    Sends regular status updates to the central server.
"""
async def sensor():
    
    # connect to the server
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
        # Read in the sensor name
        sens_name = input('Input Sensor name: ')
        # Read in the sensor type
        sens_type = input('Sensor type: ')
        # Send initialisation message to the server
        msg = '1' + ',' + sens_name + ',' + sens_type
        await websocket.send(msg)
        while True:
            
            # for simulation purposes only: this generates random values for the sensor
            if type == "ProximitySensor":
                sens_value = random.random()
            else:
                sens_value = random.getrandbits(1)
            print(sens_value)
            # (stating that this is sensor data, name , value)
            data = '0,' + sens_name + ',' + str(sens_value)
            # sends new status to the server
            await websocket.send(data)
            await asyncio.sleep(1)

asyncio.get_event_loop().run_until_complete(sensor())
