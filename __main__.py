#!/usr/bin/python
from MCP3008 import MCP3008
from Joystick import Joystick
from Events import events, eventHandler
import uinput
import time

# Instantiate MCP3008 class to assist with SPI communication to the MCP3008 chip
mcp3008 = MCP3008()

# Instantiate Joystick class to define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
left_joystick = Joystick()
right_joystick = Joystick(3, 4, 5)

# Time delay, which tells how many seconds the value is read out
delay = 0.5

mcp3008.open()

def getBtnInput(btnVal):
    return 1 if btnVal < 500 else 0

with uinput.Device(events, name="virtual-joystick") as device:
    try:
        # endless loop
        while True:
            # Determine position
            left_joystick_swt_value = mcp3008.read(left_joystick.swt)
            right_joystick_swt_value = mcp3008.read(right_joystick.swt)
            gamepadValues = (
                # Left Joystick
                1000 - mcp3008.read(left_joystick.vrx),
                mcp3008.read(left_joystick.vry),
                left_joystick_swt_value,
                # Right Joystick
                1000 - mcp3008.read(right_joystick.vrx),
                mcp3008.read(right_joystick.vry),
                left_joystick_swt_value,
                # A, B, X, Y Buttons
                getBtnInput(left_joystick_swt_value),
                getBtnInput(left_joystick_swt_value),
                getBtnInput(left_joystick_swt_value),
                getBtnInput(left_joystick_swt_value),
                # D-Pad Buttons
                getBtnInput(right_joystick_swt_value),
                getBtnInput(right_joystick_swt_value),
                getBtnInput(right_joystick_swt_value),
                getBtnInput(right_joystick_swt_value)
            )
            eventHandler(device, gamepadValues)
            # Wait
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Gamepad loop terminated...")
        pass

mcp3008.close()
print("MCP3008 connection terminated...")