#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:55:22 2022

@author: farmbot-controler
"""

from farmbot import Farmbot, FarmbotToken
import time
import csv

# Before we begin, we must download an access token from the
# API. To avoid copy/pasting passwords, it is best to create
# an access token and then store that token securely:
raw_token = FarmbotToken.download_token("test@gmail.com",
                                        "test",
                                        "http://10.42.0.1")

# This token is then passed to the Farmbot constructor:
fb = Farmbot(raw_token)

# If you are just doing testing, such as local development,
# it is possible to skip token creation and login with email
# and password. This is not recommended for production devices:
# fb = Farmbot.login(email="em@i.l",
#                    password="pass",
#                    server="https://my.farm.bot")

# The next step is to call fb.connect(), but we are not ready
# to do that yet. Before we can call connect(), we must
# create a "handler" object. FarmBot control is event-based
# and the handler object is responsible for integrating all
# of those events into a custom application.
#
# At a minimum, the handler must respond to the following
# methods:
#     on_connect(self, bot: Farmbot, client: Mqtt) -> None
#     on_change(self, bot: Farmbot, state: Dict[Any, Any]) -> None
#     on_log(self, _bot: Farmbot, log: Dict[Any, Any]) -> None
#     on_error(self, _bot: Farmbot, _response: ErrorResponse) -> None
#     on_response(self, _bot: Farmbot, _response: OkResponse) -> None
#
# FarmBotPy will call the appropriate method whenever an event
# is triggered. For example, the method `on_log` will be
# called with the last log message every time a new log
# message is created.

#DEFINING THE POINTS OF THE DOMAIN:
A =[[1000,615,-300],
    [1000,1315,-300],
    [1000,2015,-300],
    [1700,615,-300],
    [1700,1315,-300],
    [1700,2015,-300],
    [2400,615,-300],
    [2400,1315,-300],
    [2400,2015,-300],
    [3100,615,-300],
    [3100,1315,-300],
    [3100,2015,-300],
    [3800,615,-300],
    [3800,1315,-300],
    [3800,2015,-300],
    [4500,615,-300],
    [4500,1315,-300],
    [4500,2015,-300]]


#location of the tools: the z coordinate must be set when the tool is 100% attached! the descent to collect the tool must be slower and controlled!
B =[[7.6,1361.6,-371],  #soil sensor
    [7.6,1462.6,-371],  #watering nozzle
    [7.6,1562.6,-371],  #weeder
    [7.6,1667.6,-371],  #seeder
    [7.6,1767,0],  #seed tray (must be differentiated)
    [0,1867.6,-322],#seed bin
    [0,0,0]]  # Home

def extract_data(message):
    length = len(message)
    data = ""
    for i in range(length):
        if message[i].isdigit():
            data = data + message[i]
    return data




class MyHandler:
    # The `on_connect` event is called whenever the device
    # connects to the MQTT server. You can place initialization
    # logic here.
    #
    # The callback is passed a FarmBot instance, plus an MQTT
    # client object (see Paho MQTT docs to learn more).
    def __init__(self):
        
        with open('sequence.txt') as f:
        	lines = f.read()
        	f.close()
            
        cmds = lines.split("\n")
        
        self.executing = 0
        self.cnt=226
        self.id='first_id'
        self.cmds = cmds
        self.data = []
        self.pos = (0,0,0)
    def on_connect(self, bot, mqtt_client):
        # Once the bot is connected, we can send RPC commands.
        # Every RPC command returns a unique, random request
        # ID. Later on, we can use this ID to track our commands
        # as they succeed/fail (via `on_response` / `on_error`
        # callbacks):
        self.id= bot.go_to_home()
        print("GO_TO_HOME REQUEST ID: " + self.id)
        
        
        
    def on_change(self, bot, state):
        # The `on_change` event is most frequently triggered
        # event. It is called any time the device's internal
        # state changes. Example: Updating X/Y/Z position as
        # the device moves across the garden.
        # The bot maintains all this state in a single JSON
        # object that is broadcast over MQTT constantly.
        # It is a very large object, so we are printing it
        # only as an example.
        #print("NEW BOT STATE TREE AVAILABLE:")
        #print(state)
        # Since the state tree is very large, we offer
        # convenience helpers such as `bot.position()`,
        # which returns an (x, y, z) tuple of the device's
        # last known position:
        #print("Current position: (%.2f, %.2f, %.2f)" % bot.position())
        # A less convenient method would be to access the state
        # tree directly:
        pos = state["location_data"]["position"]
        xyz = (pos["x"], pos["y"], pos["z"])
        self.pos = xyz
        #print("Same information as before: " + str(xyz))

    # The `on_log` event fires every time a new log is created.
    # The callback receives a FarmBot instance, plus a JSON
    # log object. The most useful piece of information is the
    # `message` attribute, though other attributes do exist.
    
    # the robot will send the value of the SoilSensor usign this 
    # on_log function
    def on_log(self, bot, log):
        print("New message from FarmBot: " + log['message'])
        self.data.append(["Soil Sensor ",extract_data(log['message']),self.pos])

        # open the file in the write mode
        with open('data.csv', 'w') as f:
            
            writer = csv.writer(f)
            writer.writerows(self.data)
            f.close()




        
    # When a response succeeds, the `on_response` callback
    # fires. This callback is passed a FarmBot object, as well
    # as a `response` object. The most important part of the
    # `response` is `response.id`. This `id` will match the
    # original request ID, which is useful for cross-checking
    # pending operations.
    def on_response(self, bot, response):
        if self.id==response.id:
            print('cnt', self.cnt)
            program = self.cmds[self.cnt]
            exec(program)
            program = self.cmds[self.cnt+1]
            exec(program)
            self.cnt+=2
            
        print("ID of successful request: " + response.id)

    # If an RPC request fails (example: stalled motors, firmware
    # timeout, etc..), the `on_error` callback is called.
    # The callback receives a FarmBot object, plus an
    # ErrorResponse object.
    def on_error(self, bot, response):
        # Remember the unique ID that was returned when we
        # called `move_absolute()` earlier? We can cross-check
        # the ID by calling `response.id`:
        print("ID of failed request: " + response.id)
        # We can also retrieve a list of error message(s) by
        # calling response.errors:
        print("Reason(s) for failure: " + str(response.errors))


# Now that we have a handler class to use, let's create an
# instance of that handler and `connect()` it to the FarmBot:
handler = MyHandler()

# Keep in mind that `connect()` will block the current thread.
# If you require parallel operations, consider using a background
# thread or a worker process.
fb.connect(handler)
print("This line will not execute. `connect()` is a blocking call.")

