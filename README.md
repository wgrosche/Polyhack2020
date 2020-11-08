# Polyhack2020
Relevant Files are in the folder Final_Submission

Repository for the team Cache Money in the 2020 Polyhack

The code consists of four main parts: Classes.py, server_test.py, config.py and
the client_actuator and client_sensor files.


Classes.py holds the necessary classes, such as the server, the sensors and
actuators and the subclasses thereof.

The config file config.py is the set of rules that the server's rule engine
runs on. These rules are arbitrary and can be updated while the server is
running. It is according to these rules that the server evaluates the data
it receives from sensors and determines the appropriate actions to be taken
w.r.t. to the actuator statuses.

The file server_test initializes the server object, which runs the centralized
process. It keeps the server status (i.e. the current values of the device
attributes), receives data from sensors and determines the changes to be made to
the actuator values, then pushes these updated values to the actuators via a
websocket connection.

The files client_actuator and client_sensor simulate client-side behavior.
Client_sensor sends random values to the server in accordance with the sensor
type, and client_actuator acts on the messages from the server, changing its
state as the server commands.

A video demonstration of the server operation is included in the form of the file: demo.mp4
