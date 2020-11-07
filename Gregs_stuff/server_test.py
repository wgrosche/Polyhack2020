import asyncio
import websockets
import ruleset as rules
import config

async def rule_engine(websocket, path):

    config.init_sensors()

    for in range(20):
        try:
            data = await websocket.recv()
            data = data.split(',') # First entry: Sensor name, Second Entry: Value
            # now i want to update the sensor:
            eval('data[0]').value = float(data[1])
            await asyncio.sleep(0.2)

        except websockets.ConnectionClosed:
            print(f"Terminated")
            break



start_server = websockets.serve(rule_engine, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
