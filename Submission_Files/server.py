import asyncio
import websockets
import classes
import config
import importlib
import json
global server

server = classes.Server()

"""
Server for the ASUS PolyHack Challenge:
    Stores the sensor and actuator states in a Dict. Updates status based on sensor readings and pushes status to devices.
    
"""


async def rule_engine(websocket, path):
    sensors = []
    actuators = []

    while True:
        data = ['3']
        for i in range(5):
            try:
                try:
                    # information from the latest sensor push is received by the server and split into a list
                    # First entry: Sensor name, Second Entry: Value
                    data = await asyncio.wait_for(asyncio.gather(websocket.recv()),timeout = 0.5)
                    data = data[0].split(',') 
                    # if no data is received: skip this step
                except asyncio.TimeoutError:
                    pass

                if data[0] == '0':
                    # server side value of the sensor is updated
                    server.devices[data[1]].value = float(data[2])
                    
                elif data[0] == '1': # add a new sensor
                    server.ServerAddDevices(data)
                    importlib.reload(config) # reload the config to accommodate new update rules
                    sensors.append(data[1])
                    print(sensors)
                    
                elif data[0] == '2': # add a new actuator
                    server.status[data[1]] = False # set the initial value for each actuator to false
                    server.ServerAddDevices(data)
                    importlib.reload(config) # reload the config to accommodate new update rules
                    actuators.append(data[1])
                    print(actuators)
                    
                elif data[0] == '3':
                    pass

            except asyncio.TimeoutError:
                pass

            except websockets.ConnectionClosed:
                pass

        # reload the config to accommodate new update rules
        importlib.reload(config) 
        # server updates the status
        config.updates(server)
        # status is encoded using json
        status_string = json.dumps(server.status) #data serialized
        # status serialisation is sent to the clients
        await websocket.send(status_string)
        await asyncio.sleep(2)


start_server = websockets.serve(rule_engine, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
