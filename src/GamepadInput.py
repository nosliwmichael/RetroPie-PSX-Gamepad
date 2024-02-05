#!/usr/bin/env python3

from ast import literal_eval

class GamepadInput:
    def __init__(self, name: str, event_code: str, channel: int, port: str = "A", is_digital: bool = False, value: int = 0, prev_value: int = 0):
        self.name = name
        self.event_code = literal_eval(event_code)
        self.channel = channel
        self.port = port
        self.is_digital = is_digital
        self.value = value
        self.prev_value = prev_value