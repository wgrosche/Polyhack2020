"""
Config file: To be altered by the end user to accommodate their use case. Allows the implementation of:
    simple propositional logic
    fuzzy-logic
    many to one rules
    one to many rules
    
    Examples for each of the above are given.
    The update function is called by the host server and alters the status of the server before this is pushed to the devices.
    
"""

def updates(server):
    # example update rules for the server based on examples given in the ASUS project brief

    # example: Simple Propositional
    try:
        server.devices["StreetLamp"].value = server.devices["StreetLampSensor"].value
        server.status["StreetLamp"] = server.devices["StreetLampSensor"].value
        print(server.devices["StreetLamp1"].value)
    except KeyError:
        pass

    # example: Simple Fuzzy-logic
    try:
        server.devices["CatDoor"].value = server.devices["CatProximity"].value <= 0.5
        server.status["CatDoor"] = server.devices["CatDoor"].value
        print(server.devices["CatDoor"].value)
    except KeyError:
        pass

    # example: Multiple Inputs
    try:
        server.devices["Lamp"].value = server.devices["FloodlightMotionSensor"].value and server.devices["FloodlightNoiseDetector"].value
        server.status["Lamp"] = server.devices["Lamp"].value
        print(server.devices["Lamp"].value)
    except KeyError:
        pass
    
    # example: Multiple Outputs
    try:
        sens = server.devices["MuseumMotionSensor"].value
        server.devices["MuseumLamp1"].value = sens
        server.devices["MuseumLamp2"].value = sens
        server.devices["MuseumLamp3"].value = sens
        server.status["MuseumLamp1"] = server.devices["MuseumLamp3"].value
        server.status["MuseumLamp2"] = server.devices["MuseumLamp3"].value
        server.status["MuseumLamp3"] = server.devices["MuseumLamp3"].value

        print(sens)
    except KeyError:
        pass
