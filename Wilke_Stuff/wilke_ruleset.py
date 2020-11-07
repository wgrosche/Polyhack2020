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
    def client_init(device_name, device_type):
        
    def update(self):
        self.value = websockets.recv
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
        self.value = 0
        
class DoorLock(Actuator):
    def __init__(self):
        super().__init__()
        self.value = False
        

class Server(BroadcastServer):
    def __init__(self):
        super().__init__()
        self.devices = pd.DataFrame(np.zeros(,3), columns=['Device Name', 'Device Type', 'Device Value'])
        
            
    def ServerAddDevices(self):
        self.devices= ws.recv() #add devices based on d
        for device in self.devices.index:
            
    def ServerUpdate(self):
        for device in self.devices.index:
            device.update()
    
        
        