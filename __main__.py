#!/usr/bin/python
from MCP3008 import MCP3008
from Joystick import Joystick
import time
import keyboard

# Instantiate MCP3008 class to assist with SPI communication to the MCP3008 chip
mcp3008 = MCP3008()

# Instantiate Joystick class to define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
left_joystick = Joystick()
right_joystick = Joystick(3, 4, 5)

# Time delay, which tells how many seconds the value is read out
delay = 0.5

with mcp3008.open():
    # endless loop
    while not keyboard.is_pressed('esc'):
        # Determine position
        left_vrx_pos = mcp3008.read(left_joystick.vrx)
        left_vry_pos = mcp3008.read(left_joystick.vry)
        right_vrx_pos = mcp3008.read(right_joystick.vrx)
        right_vry_pos = mcp3008.read(right_joystick.vry)
        # Determine SW state
        left_swt_val = mcp3008.read(left_joystick.swt)
        right_swt_val = mcp3008.read(right_joystick.swt)
        # Print positions / states
        print("L_VRx : {} L_VRy : {} L_SW : {}".format(left_vrx_pos, left_vry_pos, left_swt_val))
        print("R_VRx : {} R_VRy : {} R_SW : {}".format(right_vrx_pos, right_vry_pos, right_swt_val))
        # Wait
        time.sleep(delay)