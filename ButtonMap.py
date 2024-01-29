#!/usr/bin/python

# DPAD_UP = 27
# DPAD_DOWN = 23
# DPAD_LEFT = 22
# DPAD_RIGHT = 17
# BTN_A = 6
# BTN_B = 24
# BTN_X = 5
# BTN_Y = 25

class ButtonMap:
    def __init__(self, up = 27, down = 23, left = 22, right = 17, a = 6, b = 24, x = 5, y = 25):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.a = a
        self.b = b
        self.x = x
        self.y = y