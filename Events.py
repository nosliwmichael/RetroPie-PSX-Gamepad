import uinput
from GamepadMap import GamepadMap
from GamepadInput import GamepadInput
import RPi.GPIO as GPIO
from MCP3008 import MCP3008
from MCP23017 import MCP23017

# TODO: Clean up events & event_map variables

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
    "BTN_TR2": uinput.BTN_TR2,
    "BTN_MODE": uinput.BTN_MODE
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
    uinput.BTN_TR2,
    uinput.BTN_MODE
)

# The order of events handled must match the events tuple above
def event_handler(virtual_gamepad: uinput.Device, 
                 mcp3008: MCP3008,
                 mcp23017: MCP23017,
                 gamepad_map: GamepadMap):
    gpio_event_handler(virtual_gamepad, gamepad_map)
    mcp3008_event_handler(virtual_gamepad, mcp3008, gamepad_map)
    mcp23017_event_handler(virtual_gamepad, mcp23017, gamepad_map)
    virtual_gamepad.syn()

def gpio_event_handler(gamepad: uinput.Device, 
                       gamepad_map: GamepadMap):
    for input in gamepad_map.gpio_inputs:
        input.value = convertDigitalBtnValue(GPIO.input(input.channel))
        if (input.value != input.prev_value):
            printInput(input)
            # gamepad.emit(event_map[input.name], input.value, syn=False)
            gamepad.emit(input.event_code, input.value, syn=False)
            input.prev_value = input.value

def mcp3008_event_handler(gamepad: uinput.Device, 
                          mcp3008: MCP3008, 
                          gamepad_map: GamepadMap):
    for input in gamepad_map.mcp3008_inputs:
        analog_value = mcp3008.read(input.channel)
        input.value = convertAnalogBtnValue(analog_value) if input.is_digital else analog_value
        if (input.value != input.prev_value):
            printInput(input)
            # gamepad.emit(event_map[input.name], input.value, syn=False)
            gamepad.emit(input.event_code, input.value, syn=False)
            input.prev_value = input.value

def mcp23017_event_handler(gamepad: uinput.Device, 
                           mcp23017: MCP23017,
                           gamepad_map: GamepadMap):
    portA = [convertDigitalBtnValue(x) for x in mcp23017.readGPIO("A")]
    portB = [convertDigitalBtnValue(x) for x in mcp23017.readGPIO("B")]
    for input in gamepad_map.mcp23017_inputs:
        input.value = portA[input.channel] if input.port == "A" else portB[input.channel]
        if (input.value != input.prev_value):
            printInput(input)
            printPorts(portA, portB)
            # gamepad.emit(event_map[input.name], input.value, syn=False)
            gamepad.emit(input.event_code, input.value, syn=False)
            input.prev_value = input.value

# Used if a digital input is passing through an ADC. Convert the value to 1 or 0
def convertAnalogBtnValue(btnVal: int) -> int:
    return 1 if btnVal < 512 else 0

# Invert the value because the pull-up resistor causes the depressed value to 
# be 1 and the pressed value to be 0
def convertDigitalBtnValue(btnVal: int) -> int:
    return 1 if btnVal == 0 else 0

def printInput(input: GamepadInput):
    #print(vars(input))
    pass

def printPorts(portA, portB):
    #print("PORT A: {}".format(portA))
    #print("PORT B: {}".format(portB))
    pass