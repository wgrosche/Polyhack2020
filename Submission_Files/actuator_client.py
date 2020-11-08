import asyncio
import websockets
import json

"""
Actuator Client for the ASUS PolyHack Challenge:
    Can take actuator types as per the ruleset file. These are Light(Continuous), DoorLock(Discrete)
    Status is updated by the server.
"""
async def actuator():
    
    # connect to the server
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
        # Read in the sensor name
        act_name = input('Input Actuator name: ')
        # Read in the sensor type
        act_type = input('Actuator type: ')
        # Send initialisation message to the server
        msg = '2' + ',' + act_name + ',' + act_type
        await websocket.send(msg)

        while True:
            
            # receive new status from the server
            message = await websocket.recv()
            # decode status update
            state = json.loads(message)
            # update status for the actuator
            try:
                state = state[act_name]
            except KeyError:
                pass
            # passes the state of the actuator
            print(state)


asyncio.get_event_loop().run_until_complete(actuator())
