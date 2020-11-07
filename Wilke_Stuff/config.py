# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:29:06 2020

@author: wilke
"""

import wilke_ruleset as rules

class Ruleset():
    def __init__(self):
        
        self.Light1 = rules.Light()
    
        self.Sensor1 = rules.MotionSensor()
        self.Sensor2 = rules.MotionSensor()

    def update(self):
        self.Light1.update((self.Sensor1.value or self.Sensor2.value))
        