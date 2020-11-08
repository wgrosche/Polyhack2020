# Polyhack2020
Repository for the team Cache Money in the 2020 Polyhack

The code consists of four main parts: classes.py, server.py, config.py and
the actuator_client.py and sensor_client.py files.

The file classes.py holds the necessary classes, such as the server, the sensors and
actuators and the subclasses thereof.

The config file config.py is the set of rules that the server's rule engine
runs on. These rules are arbitrary and can be updated while the server is
running. It is according to these rules that the server evaluates the data
it receives from sensors and determines the appropriate actions to be taken
with respect to to the actuator statuses.

The file server.py initializes the server object, which runs the centralized
process. It keeps the server status (i.e. the current values of the device
attributes), receives data from sensors and determines the changes to be made to
the actuator values, then pushes these updated values to the actuators via a
websocket connection.

The files actuator_client.py and sensor_client.py simulate client-side behavior.
sensor_client.py sends random values to the server in accordance with the sensor
type, and actuator_client.py acts on the messages from the server, changing its
state as the server commands.
