#!/usr/bin/env python3

from GamepadMap import GamepadMap

for btn in GamepadMap().gpio_inputs:
    print("name: {}, event_code: {}, channel: {}, is_digital: {}, value: {}, prev_value: {}"
          .format(btn.name, btn.event_code, btn.channel, btn.is_digital, btn.value, btn.prev_value))
    
for btn in GamepadMap().mcp3008_inputs:
    print("name: {}, event_code: {}, channel: {}, is_digital: {}, value: {}, prev_value: {}"
          .format(btn.name, btn.event_code, btn.channel, btn.is_digital, btn.value, btn.prev_value))
    
for btn in GamepadMap().mcp23017_inputs:
    print("name: {}, event_code: {}, channel: {}, is_digital: {}, value: {}, prev_value: {}"
          .format(btn.name, btn.event_code, btn.channel, btn.is_digital, btn.value, btn.prev_value))