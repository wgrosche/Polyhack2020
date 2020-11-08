# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:39:51 2020

@author: wilke
"""

class Sensor():
    def __init__(self , name = 'Sensor'):
        self.name=name
        pass

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

class DoorLock(Actuator):
    def __init__(self):
        super().__init__()
        self.value = False

DeviceDict = {"MotionSensor": MotionSensor, "ProximitySensor": ProximitySensor,
              "SmartNoiseDetector": SmartNoiseDetector, "Light": Light, "DoorLock": DoorLock}

class Server():

    def __init__(self):
        super().__init__()
        self.devices = {}
        self.status = {}

    # adds devices to the server one by one
    def ServerAddDevices(self, device_props):
        print(self.devices)
        self.devices[device_props[1]] = DeviceDict[device_props[2]]()
        print(self.devices)

    # updates the current values of the devices on the server side
    def ServerUpdate(self):
        for device in self.devices.index:
            device.update()
