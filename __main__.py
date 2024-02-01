#!/usr/bin/env python3

from MCP3008 import MCP3008
from GamepadMap import GamepadMap
from Events import events, eventHandler
import RPi.GPIO as GPIO
import uinput
import time

# Instantiate MCP3008 class to assist with SPI communication to the MCP3008 chip
mcp3008 = MCP3008()

gamepad_map = GamepadMap()

# GPIO Button Mapping
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for input in gamepad_map.gpio_inputs:
    GPIO.setup(input.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Time delay, which tells how many seconds the value is read out
delay = 0.5

mcp3008.open()

def printGamepad(gamepad_map: GamepadMap):
    gpio_str = ""
    for input in gamepad_map.gpio_inputs:
        gpio_str.join(input.name, ": ", input.value, ", ")
    print(gpio_str)

    mcp3008_str = ""
    for input in gamepad_map.mcp3008_inputs:
        gpio_str.join(input.name, ": ", input.value, ", ")
    print(mcp3008_str)

with uinput.Device(events, name="Xbox One", vendor=3695, product=313) as virtual_gamepad:
    try:
        while True:
            printGamepad(gamepad_map)
            eventHandler(virtual_gamepad, mcp3008=mcp3008, gamepad_map=gamepad_map)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Gamepad loop terminated...")
        pass

mcp3008.close()
print("MCP3008 connection terminated...")