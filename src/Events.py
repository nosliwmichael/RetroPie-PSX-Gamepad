from uinput import Device
from GamepadMap import GamepadMap
from GamepadInput import GamepadInput
import RPi.GPIO as GPIO
from MCP3008 import MCP3008
from MCP23017 import MCP23017

# The order of events handled must match the events tuple above
def event_handler(virtual_gamepad: Device, 
                 mcp3008: MCP3008,
                 mcp23017: MCP23017,
                 gamepad_map: GamepadMap):
    gpio_event_handler(virtual_gamepad, gamepad_map)
    mcp3008_event_handler(virtual_gamepad, mcp3008, gamepad_map)
    mcp23017_event_handler(virtual_gamepad, mcp23017, gamepad_map)
    virtual_gamepad.syn()

def gpio_event_handler(gamepad: Device, 
                       gamepad_map: GamepadMap):
    for input in gamepad_map.gpio_inputs:
        input.value = convertDigitalBtnValue(GPIO.input(input.pin))
        if (input.value != input.prev_value):
            printInput(input)
            gamepad.emit(input.event_code[:2], input.value, syn=False)
            input.prev_value = input.value

def mcp3008_event_handler(gamepad: Device, 
                          mcp3008: MCP3008, 
                          gamepad_map: GamepadMap):
    for input in gamepad_map.mcp3008_inputs:
        analog_value = mcp3008.read(input.pin)
        input.value = convertAnalogBtnValue(analog_value) if input.is_digital else analog_value
        abs_diff = abs(input.value - input.prev_value)
        if (
            (input.is_digital and input.value != input.prev_value) or
            (not input.is_digital and abs_diff > 50)
        ):
            printInput(input)
            gamepad.emit(input.event_code[:2], input.value, syn=False)
            input.prev_value = input.value

def mcp23017_event_handler(gamepad: Device, 
                           mcp23017: MCP23017,
                           gamepad_map: GamepadMap):
    portA = [convertDigitalBtnValue(x) for x in mcp23017.readGPIO("A")]
    portB = [convertDigitalBtnValue(x) for x in mcp23017.readGPIO("B")]
    for input in gamepad_map.mcp23017_inputs:
        input.value = portA[input.pin] if input.port == "A" else portB[input.pin]
        if (input.value != input.prev_value):
            printInput(input)
            printPorts(portA, portB)
            gamepad.emit(input.event_code[:2], input.value, syn=False)
            input.prev_value = input.value

# Used if a digital input is passing through an ADC. Convert the value to 1 or 0
# MCP3008 channels emit 10 bits which means the max value is 1023.
# Therefore, anything less than half is converted to 0.
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