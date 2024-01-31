#!/usr/bin/python

import configparser

GPIO_SECTION='GPIO'
MCP3008_SECTION='MCP3008'
MCP23017_SECTION='MCP23017'

class ButtonMap:
    def __init__(self):
        gamepad_configs = configparser.ConfigParser()
        gamepad_configs.read('gamepad.cfg')

        # GPIO
        self.DPAD_UP = gamepad_configs.get(GPIO_SECTION, 'DPAD_UP')
        self.DPAD_DOWN = gamepad_configs.get(GPIO_SECTION, 'DPAD_DOWN')
        self.DPAD_LEFT = gamepad_configs.get(GPIO_SECTION, 'DPAD_LEFT')
        self.DPAD_RIGHT = gamepad_configs.get(GPIO_SECTION, 'DPAD_RIGHT')
        self.A = gamepad_configs.get(GPIO_SECTION, 'A')
        self.B = gamepad_configs.get(GPIO_SECTION, 'B')
        self.X = gamepad_configs.get(GPIO_SECTION, 'X')
        self.Y = gamepad_configs.get(GPIO_SECTION, 'Y')
        
        # MCP3008
        self.LEFT_JOYSTICK_BTN = gamepad_configs.get(MCP3008_SECTION, 'LEFT_JOYSTICK_BTN')
        self.LEFT_JOYSTICK_X = gamepad_configs.get(MCP3008_SECTION, 'LEFT_JOYSTICK_X')
        self.LEFT_JOYSTICK_Y = gamepad_configs.get(MCP3008_SECTION, 'LEFT_JOYSTICK_Y')
        self.RIGHT_JOYSTICK_BTN = gamepad_configs.get(MCP3008_SECTION, 'RIGHT_JOYSTICK_BTN')
        self.RIGHT_JOYSTICK_X = gamepad_configs.get(MCP3008_SECTION, 'RIGHT_JOYSTICK_X')
        self.RIGHT_JOYSTICK_Y = gamepad_configs.get(MCP3008_SECTION, 'RIGHT_JOYSTICK_Y')

        # MCP23017
        self.START = gamepad_configs.getint(MCP23017_SECTION, 'START')
        self.SELECT = gamepad_configs.getint(MCP23017_SECTION, 'SELECT')
        self.LEFT_SHOULDER = gamepad_configs.getint(MCP23017_SECTION, 'LEFT_SHOULDER')
        self.RIGHT_SHOULDER = gamepad_configs.getint(MCP23017_SECTION, 'RIGHT_SHOULDER')
        self.LEFT_TRIGGER = gamepad_configs.getint(MCP23017_SECTION, 'LEFT_TRIGGER')
        self.RIGHT_TRIGGER = gamepad_configs.getint(MCP23017_SECTION, 'RIGHT_TRIGGER')