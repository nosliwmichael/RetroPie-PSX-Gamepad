#!/usr/bin/env python3

from MCP3008 import MCP3008
from MCP23017 import MCP23017
from GamepadMap import GamepadMap
from Events import event_handler
import RPi.GPIO as GPIO
from uinput import Device
import time

# Time delay, which tells how many seconds the value is read out
DELAY = 0.05
GAMEPAD_MAP = GamepadMap()

with MCP3008() as mcp3008, \
    MCP23017() as mcp23017, \
    Device(GAMEPAD_MAP.getEvents(), name=GAMEPAD_MAP.device_name, vendor=GAMEPAD_MAP.vendor, product=GAMEPAD_MAP.product) as virtual_gamepad:
    # GPIO Button Mapping
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for input in GAMEPAD_MAP.gpio_inputs:
        GPIO.setup(input.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        while True:
            event_handler(virtual_gamepad=virtual_gamepad, 
                         mcp3008=mcp3008, 
                         mcp23017=mcp23017, 
                         gamepad_map=GAMEPAD_MAP)
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("Gamepad loop terminated...")
        pass