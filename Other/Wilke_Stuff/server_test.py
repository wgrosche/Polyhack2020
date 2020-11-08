import asyncio
import websockets
import ruleset as rules
import config
import importlib
import wilke_ruleset as wrs

async def rule_engine(websocket, path):

    #config.init_sensors()
    sensors = []
    actuators = []
    server = wrs.Server()
    while True:
        for i in range(20):
            try:
                data = await websocket.recv()
                data = data.split(' ') # First entry: Sensor name, Second Entry: Value

                if data[0]=='0':
                    # now i want to update the sensor:
                    server.ServerUpdate()
                    print("Received: {}".format(result))
                elif data[0]=='1':
                    server.ServerAddDevices(data)


                await asyncio.sleep(0.2)

            except websockets.ConnectionClosed:
                #print(f"Terminated")
                break

        #logic phase
        config.updates()


start_server = websockets.serve(rule_engine, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
