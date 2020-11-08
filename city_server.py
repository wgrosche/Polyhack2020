#!/usr/bin/env python
import asyncio
import websockets
import numpy as np
import random as rand
import time
import datetime
import matplotlib.pyplot as plt
import city_classes

global server
server = city_classes.Server()

num_agents = 5 # number of agents
dim = 30 # grid dimension

sensors = []
lights = []
doors = []

grid = np.zeros((dim,dim))
positions = np.zeros((num_agents,2))

def initialize_grid():
    for i in range(num_agents):
        positions[i] = np.array([rand.randint(0,dim-1),rand.randint(0,dim-1)])
    update_grid()
    #plot()

def plot():
    plt.figure()
    plt.imshow(grid,cmap="Paired")
    plt.show() # better show on server

def update_grid():
    """
    empty:                0
    agent:                1
    devices: light: on:  10
                    off: -1
             sensor:      2
    """
    grid = np.zeros((dim,dim))
    for i in range(num_agents):
        grid[int(positions[i,0]),int(positions[i,1])] = 1

    for sensor in sensors:
        grid[int(sensor.position[0]),int(sensor.position[1])] = 2

    for light in lights:
        if light.light == True:
            grid[int(sensor.position[0]),int(sensor.position[1])] = 3
        else: grid[int(sensor.position[0]),int(sensor.position[1])] = -1

# initialization of sensors and lights
class light():
    def __init__(self,coordinates):
        self.location = coordinates
        self.light = False
    def update(bool):
        self.light = bool

light1 = light(np.array([rand.randint(0,dim-1),rand.randint(0,dim-1)]))
prox_sensor1 = light1.location

# measure distance of person to sensor
def prox_sensor(sensor, position):
    result = np.linalg.norm(np.array(server.devices[sensor].location)-position)
    print(result)
    return result


# random walk step
def walk(position):
    val = rand.randint(1, 4)
    x_, y_ = position[0], position[1]
    if val == 1:
        x = x_ + 1
        y = y_
    elif val == 2:
        x = x_ - 1
        y = y_
    elif val == 3:
        x = x_
        y = y_ + 1
    else:
        x = x_
        y = y_ - 1
    # exceptions
    if x>=dim or x<0 or y>=dim or y<0:
        x,y = walk(position)
    return np.array([x,y])

def gen_location():
    # Generate a random location for the sensor on the map
    return np.array([rand.randint(0,dim-1),rand.randint(0,dim-1)])

###############################################################################################
###############################################################################################

initialize_grid()


async def city_sim(websocket, path):
    while True:
        for i in range(10):
            try:
                data = await asyncio.wait_for(websocket.recv(),timeout = 1)
                data = data.split(',')
                data[0] = gen_location()
                server.ServerAddDevices(data)

            except asyncio.TimeoutError:
                for i in range(num_agents):
                    positions[i] = walk(positions[i])
                update_grid()
                #await websocket.send(plot())
                time.sleep(0.2)
            except websockets.ConnectionClosed:
                pass

        for sensor in server.devices:
            #stat = ','.join([str(num) for num in prox_sensor(sensor , positions)])
            stat = ','.join([str(prox_sensor(sensor , positions[i])) for i in range(num_agents)])
            server.status[sensor] = stat
        try:
            await websocket.send(server.status)
        except:
            pass


start_server = websockets.serve(city_sim, "127.0.0.1", 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
