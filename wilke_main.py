# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:37:20 2020

@author: wilke
"""

import websockets as wbs
import asyncio as sync
import numpy as np
import pandas as pd
import requests

# Asus PolyHack Challenge


## Ruleset
# information provided by the end user to define the
# actions taken in response certain stimuli
ruleset = ...

## Device Type
# device type defines the number of input and output arguments
# it can take based on the ruleset. sensors can read signals
# from the environment and output information to the central api server
# actuators can take input information from the central server
# and output to the environment. 
dev_type = ...






def device_request(dev_type, input_data):
    global ruleset
    
def 