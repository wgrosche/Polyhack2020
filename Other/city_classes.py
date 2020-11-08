class Sensor():
    def __init__(self , name = 'Sensor' , location = [0,0]):
        self.name=name
        self.location = location
        pass


class MotionSensor(Sensor):
    def __init__(self ,location = [0,0]):
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


    def ServerAddDevices(self, device_props):
        #device_props = string.split(",")#ws.recv().split(" ")
        print(self.devices)
        self.devices[device_props[1]] = DeviceDict[device_props[2]](location = device_props[0])
        print(self.devices)
        # if(device_props[2] == "False")


        # device_props2 = "Sensor2 ProximitySensor".split(" ")
        # self.devices.append(ws.recv()) #add devices based on d 'Sensor1', 'MotionSensor', 'False'  Sensor1 = MotionSensor()
        # self.devices
        #for device in self.devices:
            #device.DeviceName = device.DeviceType

    def ServerUpdate(self):
        for device in self.devices.index:
            device.update()
