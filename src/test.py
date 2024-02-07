#!/usr/bin/env python3

import os
from GamepadMap import GamepadMap

RP_PSX_GP_LOG = os.getenv("RP_PSX_GP_LOG", "DEBUG")
print("RP_PSX_GP_LOG: {}".format(RP_PSX_GP_LOG))
if (RP_PSX_GP_LOG == "DEBUG"):
    for btn in GamepadMap().gpio_inputs:
        print("name: {}, event_code: {}, pin: {}, is_digital: {}, value: {}, prev_value: {}"
            .format(btn.name, btn.event_code, btn.pin, btn.is_digital, btn.value, btn.prev_value))
        
    for btn in GamepadMap().mcp3008_inputs:
        print("name: {}, event_code: {}, pin: {}, is_digital: {}, value: {}, prev_value: {}"
            .format(btn.name, btn.event_code, btn.pin, btn.is_digital, btn.value, btn.prev_value))
        
    for btn in GamepadMap().mcp23017_inputs:
        print("name: {}, event_code: {}, pin: {}, is_digital: {}, value: {}, prev_value: {}"
            .format(btn.name, btn.event_code, btn.pin, btn.is_digital, btn.value, btn.prev_value))
