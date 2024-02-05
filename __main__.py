#!/usr/bin/env python3

from MCP3008 import MCP3008
from MCP23017 import MCP23017
from GamepadMap import GamepadMap
import Events
import RPi.GPIO as GPIO
import uinput
import time

# Time delay, which tells how many seconds the value is read out
DELAY = 0.05
GAMEPAD_MAP = GamepadMap()

with MCP3008() as mcp3008, \
    MCP23017() as mcp23017, \
    uinput.Device(GAMEPAD_MAP.getEvents(), name="RetroPie-PSX-Gamepad", vendor=6969, product=420) as virtual_gamepad:
    # GPIO Button Mapping
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for input in GAMEPAD_MAP.gpio_inputs:
        GPIO.setup(input.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        while True:
            Events.event_handler(virtual_gamepad=virtual_gamepad, 
                         mcp3008=mcp3008, 
                         mcp23017=mcp23017, 
                         gamepad_map=GAMEPAD_MAP)
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("Gamepad loop terminated...")
        pass