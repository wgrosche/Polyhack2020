# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:29:06 2020

@author: wilke
"""
import ruleset as rules

def init_sensors():
    Light1 = rules.Light()

    Sensor1 = rules.MotionSensor()
    Sensor2 = rules.MotionSensor()

def updates(server):

    # hier wäre es vielleicht praktisch irgendwie über die Sensoren zu loopen.
    #Wenn die Sensoren einfach durchnummeriert wären, wäre das auch nicht so schwierig.
    #Sensor1.update()
    #Sensor2.update()
    #Light1.update((Sensor1.value or Sensor2.value))

    haha = 2
    # turn on Light1 if Sensor1 or Sensor2 is active
    #print(server.devices)
    try:
        if server.devices["Sensor1"].value or server.devices["Sensor2"].value:
            server.devices["Light1"].value = True
        print(server.devices["Light1"].value)
    except KeyError:
        pass
