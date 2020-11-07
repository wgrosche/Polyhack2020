# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:39:51 2020

@author: wilke
"""

# class RuleSet():
#     def _init_(self):
#         self.sensor = False
#         self.lightswitch = False
#     def update(self):
#         if self.sensor:
#             self.lightswitch = True
#         else:
#             self.lightswitch = False
        
    
class Sensor(): 
    def __init__(self):
        pass
    # def update(self, server):
    #     pull
        
        
class MotionSensor(Sensor):
    def __init__(self):
        super().__init__()
        self.value = False
        
class SmartNoiseDetector(Sensor):
    def __init__(self):
        super().__init__()
        self.value = False

class ProximitySensor(Sensor):
    def __init__(self):
        super().__init__()
        self.value = 0
        
class Actuator():
    def __init__(self):
        pass
    def update(self, inputs):
        self.value = inputs
        

class Light(Actuator):
    def __init__(self):
        super().__init__()
        self.value = False
        

