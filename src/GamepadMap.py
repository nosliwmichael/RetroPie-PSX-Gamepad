#!/usr/bin/env python3

import os
import json
from typing import List
from GamepadInput import GamepadInput

class GamepadMap:
    def __init__(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        gamepad_json_file = os.path.join(script_directory, '..', 'gamepad.json')
        
        with open(gamepad_json_file) as file:
            gamepad_json = json.load(file)

        self.device_name = gamepad_json['DEVICE_NAME']
        self.vendor = gamepad_json['VENDOR']
        self.product = gamepad_json['PRODUCT']

        self.gpio_inputs: List[GamepadInput] = []
        self.mcp3008_inputs: List[GamepadInput] = []
        self.mcp23017_inputs: List[GamepadInput] = []

        # GPIO
        for input in gamepad_json['GPIO']:
            self.gpio_inputs.append(mapInput(input))
        
        # MCP3008
        for input in gamepad_json['MCP3008']:
            self.mcp3008_inputs.append(mapInput(input))

        # MCP23017
        for input in gamepad_json['MCP23017']:
            self.mcp23017_inputs.append(mapInput(input))
        
    def getEvents(self):
        return tuple(i.event_code for i in self.gpio_inputs) + \
                tuple(i.event_code for i in self.mcp3008_inputs) + \
                tuple(i.event_code for i in self.mcp23017_inputs)

def mapInput(config) -> GamepadInput:
    return GamepadInput(
        name=config['name'],
        event_code=config['event_code'],
        pin=config['pin'],
        port=config['port'],
        is_digital=config['is_digital']
    )