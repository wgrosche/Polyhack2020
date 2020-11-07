import asyncio
import websockets
import ruleset as rules
import config
import importlib

async def rule_engine(websocket, path):

    #config.init_sensors()
    sensors = []
    actuators = []
    while True:
        for i in range(20):
            try:
                data = await websocket.recv()
                data = data.split(',') # First entry: Sensor name, Second Entry: Value

                if data[0]=='0':
                    # now i want to update the sensor:
                    eval(data[1]).value = float(data[2])
                elif data[0]=='1':
                    #eval(data[1]) = config.eval(data[2])(name = data[1])
                    exec("%s = %d" % (data[1],config.eval(data[2])(name = data[1])))
                    importlib.reload(config)
                    sensors.append(data[1])
                    print(sensors)
                elif data[0]=='2':
                    #eval(data[1]) = config.eval(data[2])(name = data[1])
                    exec("%s = %d" % (data[1],config.eval(data[2])(name = data[1])))
                    importlib.reload(config)
                    actuators.append(data[1])
                    print(actuators)

                await asyncio.sleep(0.2)

            except websockets.ConnectionClosed:
                #print(f"Terminated")
                break

        #logic phase
        config.updates()


start_server = websockets.serve(rule_engine, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
