import uinput
from GamepadMap import GamepadMap
from GamepadInput import GamepadInput
import RPi.GPIO as GPIO
from MCP3008 import MCP3008

# https://github.com/tuomasjjrasanen/python-uinput/blob/master/src/ev.py
event_map = {
    "ABS_X" : uinput.ABS_X,                   # Left joystick X-axis
    "ABS_Y": uinput.ABS_Y,                    # Left joystick Y-axis
    "BTN_THUMBL": uinput.BTN_THUMBL,          # Left joystick button
    "ABS_RX": uinput.ABS_RX,                  # Right joystick X-axis
    "ABS_RY": uinput.ABS_RY,                  # Right joystick Y-axis
    "BTN_THUMBR": uinput.BTN_THUMBR,          # Right joystick button
    "BTN_SOUTH": uinput.BTN_SOUTH,
    "BTN_EAST": uinput.BTN_EAST,
    "BTN_WEST": uinput.BTN_WEST,
    "BTN_NORTH": uinput.BTN_NORTH,
    "BTN_DPAD_UP": uinput.BTN_DPAD_UP,
    "BTN_DPAD_DOWN": uinput.BTN_DPAD_DOWN,
    "BTN_DPAD_LEFT": uinput.BTN_DPAD_LEFT,
    "BTN_DPAD_RIGHT": uinput.BTN_DPAD_RIGHT,
    "BTN_START": uinput.BTN_START,
    "BTN_SELECT": uinput.BTN_SELECT,
    "BTN_TL": uinput.BTN_TL,
    "BTN_TR": uinput.BTN_TR,
    "BTN_TL2": uinput.BTN_TL2,
    "BTN_TR": uinput.BTN_TR2
}
events = (
    uinput.ABS_X + (0, 1023, 0, 0),   # Left joystick X-axis
    uinput.ABS_Y + (0, 1023, 0, 0),   # Left joystick Y-axis
    uinput.BTN_THUMBL,                # Left joystick button
    uinput.ABS_RX + (0, 1023, 0, 0),  # Right joystick X-axis
    uinput.ABS_RY + (0, 1023, 0, 0),  # Right joystick Y-axis
    uinput.BTN_THUMBR,                # Right joystick button
    uinput.BTN_SOUTH,
    uinput.BTN_EAST,
    uinput.BTN_WEST,
    uinput.BTN_NORTH,
    uinput.BTN_DPAD_UP,
    uinput.BTN_DPAD_DOWN,
    uinput.BTN_DPAD_LEFT,
    uinput.BTN_DPAD_RIGHT,
    uinput.BTN_START,
    uinput.BTN_SELECT,
    uinput.BTN_TL,
    uinput.BTN_TR,
    uinput.BTN_TL2,
    uinput.BTN_TR2
)

# The order of events handled must match the events tuple above
def eventHandler(virtual_gamepad: uinput.Device, 
                 mcp3008: MCP3008, 
                 gamepad_map: GamepadMap):
    for input in gamepad_map.gpio_inputs:
        input.value = readGpioPin(input)
        if (input.value != input.prev_value):
            printInput(input)
            virtual_gamepad.emit(event_map[input.name], input.value, syn=False)
            input.prev_value = input.value

    for input in gamepad_map.mcp3008_inputs:
        input.value = readAnalogChannel(mcp3008, input)
        if (
            (input.is_digital and input.value != input.prev_value) or
            (not input.is_digital)
        ):
            printInput(input)
            virtual_gamepad.emit(event_map[input.name], input.value, syn=False)
            input.prev_value = input.value

    # for input in gamepad_map.mcp23017_inputs:
    #     input.value = readGpioExpansionPin(input)
    #     if (input.value != input.prev_value):
    #         virtual_gamepad.emit(event_map[input.name], input.value, syn=False)
    #         input.prev_value = input.value
    #         printInput(input)
    
    virtual_gamepad.syn()

# Used if a digital input is passing through an ADC. Convert the value to 1 or 0
def convertAnalogBtnValue(btnVal: int) -> int:
    return 1 if btnVal < 512 else 0

# Invert the value because the pull-up resistor causes the depressed value to 
# be 1 and the pressed value to be 0
def convertDigitalBtnValue(btnVal: int) -> int:
    return 1 if btnVal == 0 else 0

def readAnalogChannel(mcp3008: MCP3008, input: GamepadInput) -> int:
    analog_value = mcp3008.read(input.channel)
    return convertAnalogBtnValue(analog_value) if input.is_digital else analog_value

def readGpioPin(input: GamepadInput) -> int:
    return convertDigitalBtnValue(GPIO.input(input.channel))

def readGpioExpansionPin(input: GamepadInput) -> int:
    return convertDigitalBtnValue(1)

def printInput(input: GamepadInput):
    print(vars(input))