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
import config 

class Device():
    def __init__(self):
        pass
    
class Sensor(Device): 
    def __init__(self):
        super().__init__()
        pass
    # def client_init(device_name, device_type):
        
    def update(self):
        pass
        # self.value = websockets.recv
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
        
class Actuator(Device):
    def __init__(self):
        super().__init__()
        pass
    def update(self, inputs):
        self.value = inputs
        

class Light(Actuator):
    def __init__(self):
        super().__init__()
        self.value = 0
    def update(self):
        super().update()
        assert ((self.value >= 0) or (self.value < 1))
                
class DoorLock(Actuator):
    def __init__(self):
        super().__init__()
        self.value = False
    def update(self):
        super().update()
        assert ((self.value == True) or (self.value == False))
     

DeviceDict = {"MotionSensor": MotionSensor, "ProximitySensor": ProximitySensor, 
              "SmartNoiseDetector": SmartNoiseDetector, "Light": Light, "DoorLock": DoorLock}

class Server():
    def __init__(self):
        super().__init__()
        self.devices = {}
        self.configuration = config.Ruleset()

            
    def ServerAddDevices(self, device_props):
        # device_props = "Sensor1 MotionSensor".split(" ")#ws.recv().split(" ")
        self.devices[device_props[1]] = DeviceDict[device_props[2]]()

        for device in self.devices:
            self.devices[device] = device.DeviceType
            
    def push(self):
        for device in self.devices:
            if isinstance(self.devices[device], Actuator):
                self.devices[device].update()
            
    def pull(self):
        for device in self.devices:
            self.devices[device].update()
            
