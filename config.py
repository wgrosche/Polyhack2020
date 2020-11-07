# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:29:06 2020

@author: wilke
"""
import ruleset as rules


Light1 = rules.Light()

Sensor1 = rules.MotionSensor()
Sensor2 = rules.MotionSensor()

Light1.update((Sensor1.value or Sensor2.value))



