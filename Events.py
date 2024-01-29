import uinput

# https://github.com/tuomasjjrasanen/python-uinput/blob/master/src/ev.py
events = (
    uinput.ABS_X + (0, 1000, 0, 0),   # Left joystick X-axis
    uinput.ABS_Y + (0, 1000, 0, 0),   # Left joystick Y-axis
    uinput.ABS_THUMBL,                # Left joystick button
    uinput.ABS_RX + (0, 1000, 0, 0),  # right joystick X-axis
    uinput.ABS_RY + (0, 1000, 0, 0),  # Right joystick Y-axis
    uinput.ABS_THUMBR,                # Right joystick button
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_X,
    uinput.BTN_Y,
    uinput.BTN_DPAD_UP,
    uinput.BTN_DPAD_DOWN,
    uinput.BTN_DPAD_LEFT,
    uinput.BTN_DPAD_RIGHT
)

# The order of events handled must match the events tuple above
def eventHandler(gamepad, values):
    # Left Joystick
    gamepad.emit(uinput.ABS_X, values[0], syn=False)
    gamepad.emit(uinput.ABS_Y, values[1], syn=False)
    gamepad.emit_click(uinput.ABS_THUMBL, values[2], syn=False)

    # Right Joystick
    gamepad.emit(uinput.ABS_RX, values[3], syn=False)
    gamepad.emit(uinput.ABS_RY, values[4], syn=False)
    gamepad.emit_click(uinput.ABS_THUMBR, values[5], syn=False)

    # A, B, X, Y Buttons
    gamepad.emit_click(uinput.BTN_A, values[6], syn=False)
    gamepad.emit_click(uinput.BTN_B, values[7], syn=False)
    gamepad.emit_click(uinput.BTN_X, values[8], syn=False)
    gamepad.emit_click(uinput.BTN_Y, values[9], syn=False)

    # D-Pad Buttons
    gamepad.emit_click(uinput.BTN_DPAD_UP, values[10], syn=False)
    gamepad.emit_click(uinput.BTN_DPAD_DOWN, values[11], syn=False)
    gamepad.emit_click(uinput.BTN_DPAD_LEFT, values[12], syn=False)
    # Final event must of syn=True
    gamepad.emit_click(uinput.BTN_DPAD_RIGHT, values[13], syn=True)