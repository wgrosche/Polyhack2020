# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:29:06 2020

@author: wilke
"""
import ruleset as rules


def updates(Server):

    # hier wäre es vielleicht praktisch irgendwie über die Sensoren zu loopen.
    #Wenn die Sensoren einfach durchnummeriert wären, wäre das auch nicht so schwierig.
    #Sensor1.update()
    #Sensor2.update()
    #Light1.update((Sensor1.value or Sensor2.value))
    # print(Server.devices)
    # haha = 2
    # # turn on Light1 if Sensor1 or Sensor2 is active
    expected_devices = ["Sensor1", "Sensor2", "Light1"]
    for dev in expected_devices:
        try:
            Server.devices[dev]
        except NameError:
            Server.devices[dev] = 0
    if Server.devices["Sensor1"].value or Server.devices["Sensor2"].value:
        Server.devices["Light1"].value = True
                
        # print(Light1.value)
