import asyncio
import websockets
import ruleset as rules
import config
import importlib
import json
global server

server = rules.Server()




async def rule_engine(websocket, path):

    #config.init_sensors()
    sensors = []
    actuators = []

    while True:
        data = ['3']
        for i in range(9):
            try:
                try:
                    data = await asyncio.wait_for(asyncio.gather(websocket.recv()),timeout = 0.5)
                    print(data)
                    data = data[0].split(',') # First entry: Sensor name, Second Entry: Value
                except asyncio.TimeoutError:
                    pass
                #data = await websocket.recv()
                #data = data.split(',') # First entry: Sensor name, Second Entry: Value

                if data[0] == '0':
                    # now i want to update the sensor:
                    server.devices[data[1]].value = float(data[2])
                elif data[0] == '1':
                    #eval(data[1]) = config.eval(data[2])(name = data[1])
                    #class_ = getattr(rules , data[2])
                    #exec("%s = %d" % (data[1],class_()))
                    #exec("%s = %d" % (data[1],rules.eval(data[2])(name = data[1])))

                    server.ServerAddDevices(data)

                    importlib.reload(config)
                    sensors.append(data[1])
                    print(sensors)
                elif data[0] == '2':
                    #eval(data[1]) = config.eval(data[2])(name = data[1])
                    #class_ = getattr(rules , data[2])
                    #exec("%s = %d" % (data[1],class_()))
                    #exec("%s = %d" % (data[1],rules.eval(data[2])(name = data[1])))

                    server.status[data[1]] = False
                    server.ServerAddDevices(data)

                    importlib.reload(config)
                    actuators.append(data[1])
                    print(actuators)
                elif data[0] == '3':
                    pass

                #await asyncio.sleep(1)

            except asyncio.TimeoutError:
                pass

            except websockets.ConnectionClosed:
                #print(f"Terminated")
                pass

        #logic phase
        importlib.reload(config)
        config.updates(server)
        # websocket.connections.itervalues():

        # for actuator in actuators:
        #     await websocket.send(server.status[actuator])
        status_string = json.dumps(server.status) #data serialized
        print(status_string)
        await websocket.send(status_string)
        await asyncio.sleep(2)


start_server = websockets.serve(rule_engine, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
