#!/usr/bin/python

import os
import configparser

GPIO_SECTION='GPIO'
MCP3008_SECTION='MCP3008'
MCP23017_SECTION='MCP23017'

class ButtonMap:
    def __init__(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_directory, 'gamepad.cfg')
        gamepad_configs = configparser.ConfigParser()
        print(config_file_path)
        gamepad_configs.read(config_file_path)

        # GPIO
        self.DPAD_UP = gamepad_configs.getint(GPIO_SECTION, 'DPAD_UP')
        self.DPAD_DOWN = gamepad_configs.getint(GPIO_SECTION, 'DPAD_DOWN')
        self.DPAD_LEFT = gamepad_configs.getint(GPIO_SECTION, 'DPAD_LEFT')
        self.DPAD_RIGHT = gamepad_configs.getint(GPIO_SECTION, 'DPAD_RIGHT')
        self.A = gamepad_configs.getint(GPIO_SECTION, 'A')
        self.B = gamepad_configs.getint(GPIO_SECTION, 'B')
        self.X = gamepad_configs.getint(GPIO_SECTION, 'X')
        self.Y = gamepad_configs.getint(GPIO_SECTION, 'Y')
        
        # MCP3008
        self.LEFT_JOYSTICK_BTN = gamepad_configs.getint(MCP3008_SECTION, 'LEFT_JOYSTICK_BTN')
        self.LEFT_JOYSTICK_X = gamepad_configs.getint(MCP3008_SECTION, 'LEFT_JOYSTICK_X')
        self.LEFT_JOYSTICK_Y = gamepad_configs.getint(MCP3008_SECTION, 'LEFT_JOYSTICK_Y')
        self.RIGHT_JOYSTICK_BTN = gamepad_configs.getint(MCP3008_SECTION, 'RIGHT_JOYSTICK_BTN')
        self.RIGHT_JOYSTICK_X = gamepad_configs.getint(MCP3008_SECTION, 'RIGHT_JOYSTICK_X')
        self.RIGHT_JOYSTICK_Y = gamepad_configs.getint(MCP3008_SECTION, 'RIGHT_JOYSTICK_Y')

        # MCP23017
        self.START = gamepad_configs.getint(MCP23017_SECTION, 'START')
        self.SELECT = gamepad_configs.getint(MCP23017_SECTION, 'SELECT')
        self.LEFT_SHOULDER = gamepad_configs.getint(MCP23017_SECTION, 'LEFT_SHOULDER')
        self.RIGHT_SHOULDER = gamepad_configs.getint(MCP23017_SECTION, 'RIGHT_SHOULDER')
        self.LEFT_TRIGGER = gamepad_configs.getint(MCP23017_SECTION, 'LEFT_TRIGGER')
        self.RIGHT_TRIGGER = gamepad_configs.getint(MCP23017_SECTION, 'RIGHT_TRIGGER')

print(vars(ButtonMap()))