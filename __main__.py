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
    GPIO.setup(input.component.channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Time delay, which tells how many seconds the value is read out
delay = 0.05

mcp3008.open()

def printGamepad(gamepad):
    print("Lx: {}, Ly: {}, L1: {}, Rx: {}, Ry: {}, R1: {}".format(
        gamepad[0], gamepad[1], gamepad[2], gamepad[3], gamepad[4], gamepad[5]))
    print("a: {}, b: {}, x: {}, y: {}".format(
        gamepad[6], gamepad[7], gamepad[8], gamepad[9]))
    print("dU: {}, dD: {}, dL: {}, dR: {}".format(
        gamepad[10], gamepad[11], gamepad[12], gamepad[13]))

with uinput.Device(events, name="Xbox One", vendor=3695, product=313) as virtual_gamepad:
    try:
        while True:
            #printGamepad(gamepadValues)
            eventHandler(virtual_gamepad, gamepad=gamepad_map)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Gamepad loop terminated...")
        pass

mcp3008.close()
print("MCP3008 connection terminated...")