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


    # turn on Light1 if Sensor1 or Sensor2 is active
    #print(server.devices)
    try:
        if server.devices["Sensor1"].value or server.devices["Sensor2"].value:
            server.devices["Light1"].value = True
            server.status["Light1"] = True
        print(server.devices["Light1"].value)
    except KeyError:
        pass

    try:
        if server.devices["Sensor1"].value and server.devices["Sensor2"].value:
            server.devices["Light2"].value = True
            server.status["Light2"] = True
        print(server.devices["Light2"].value)
    except KeyError:
        pass

    try:
        if server.devices["Sensor1"].value and server.devices["Sensor2"].value:
            server.devices["Light3"].value = True
            server.status["Light3"] = True
        print(server.devices["Light3"].value)
    except KeyError:
        pass

    try:
        if ((server.devices["Prox1"].value < 1) and server.devices["Sensor1"].value):
            server.devices["LightCont"].value = server.devices["Prox1"].value
            server.status["LightCont"] = server.devices["Light"].value
        print(server.devices["LightCont"].value)
    except KeyError:
        pass
