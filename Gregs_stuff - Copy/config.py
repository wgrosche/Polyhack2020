# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:29:06 2020

@author: wilke
"""
import ruleset as rules

def __init__():
    pass
def update():
    for actuator in actuators:
        actuator.update()
    # hier wäre es vielleicht praktisch irgendwie über die Sensoren zu loopen.
    #Wenn die Sensoren einfach durchnummeriert wären, wäre das auch nicht so schwierig.
    #Sensor1.update()
    #Sensor2.update()
    haha = 2
    #Light1.update((Sensor1.value or Sensor2.value))
