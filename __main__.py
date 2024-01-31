#!/usr/bin/python
from MCP3008 import MCP3008
from Joystick import Joystick
from ButtonMap import ButtonMap
from Events import events, eventHandler
import RPi.GPIO as GPIO
import uinput
import time

# Instantiate MCP3008 class to assist with SPI communication to the MCP3008 chip
mcp3008 = MCP3008()

button_map = ButtonMap()

# GPIO Button Mapping
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_map.DPAD_UP, GPIO.IN)
GPIO.setup(button_map.DPAD_DOWN, GPIO.IN)
GPIO.setup(button_map.DPAD_LEFT, GPIO.IN)
GPIO.setup(button_map.DPAD_RIGHT, GPIO.IN)
GPIO.setup(button_map.A, GPIO.IN)
GPIO.setup(button_map.B, GPIO.IN)
GPIO.setup(button_map.X, GPIO.IN)
GPIO.setup(button_map.Y, GPIO.IN)

# Instantiate Joystick class to define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
left_joystick = Joystick(button_map.LEFT_JOYSTICK_BTN, button_map.LEFT_JOYSTICK_X, button_map.LEFT_JOYSTICK_Y)
right_joystick = Joystick(button_map.RIGHT_JOYSTICK_BTN, button_map.RIGHT_JOYSTICK_X, button_map.RIGHT_JOYSTICK_Y)

# Time delay, which tells how many seconds the value is read out
delay = 0.05

mcp3008.open()

def convertAnalogBtnValue(btnVal):
    return 1 if btnVal < 500 else 0

def convertDigitalBtnValue(btnVal):
    return 1 if btnVal == 0 else 0

def readChannel(adcChannel):
    return mcp3008.read(adcChannel.channel)

def updateJoystickValues(joystick):
    joystick.swtValue = convertAnalogBtnValue(readChannel(joystick.swtChannel))
    joystick.vryValue = readChannel(joystick.vryChannel)
    joystick.vrxValue = readChannel(joystick.vrxChannel)

def printGamepad(gamepad):
    print("Lx: {}, Ly: {}, L1: {}, Rx: {}, Ry: {}, R1: {}".format(
        gamepad[0], gamepad[1], gamepad[2], gamepad[3], gamepad[4], gamepad[5]))
    print("a: {}, b: {}, x: {}, y: {}".format(
        gamepad[6], gamepad[7], gamepad[8], gamepad[9]))
    print("dU: {}, dD: {}, dL: {}, dR: {}".format(
        gamepad[10], gamepad[11], gamepad[12], gamepad[13]))

with uinput.Device(events, name="Xbox One", vendor=3695, product=313) as device:
    try:
        prevGamepadValues = (0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        # endless loop
        while True:
            updateJoystickValues(left_joystick)
            left_joystick.vrxValue = left_joystick.vrxValue
            updateJoystickValues(right_joystick)
            right_joystick.vrxValue = right_joystick.vrxValue
            gamepadValues = (
                # Left Joystick
                left_joystick.vrxValue,
                left_joystick.vryValue,
                left_joystick.swtValue,
                # Right Joystick
                right_joystick.vrxValue,
                right_joystick.vryValue,
                right_joystick.swtValue,
                # A, B, X, Y Buttons
                convertDigitalBtnValue(GPIO.input(button_map.A)),
                convertDigitalBtnValue(GPIO.input(button_map.B)),
                convertDigitalBtnValue(GPIO.input(button_map.X)),
                convertDigitalBtnValue(GPIO.input(button_map.Y)),
                # D-Pad Buttons
                convertDigitalBtnValue(GPIO.input(button_map.DPAD_UP)),
                convertDigitalBtnValue(GPIO.input(button_map.DPAD_DOWN)),
                convertDigitalBtnValue(GPIO.input(button_map.DPAD_LEFT)),
                convertDigitalBtnValue(GPIO.input(button_map.DPAD_RIGHT))
            )
            #printGamepad(gamepadValues)
            eventHandler(device, gamepadValues, prevGamepadValues)
            # Wait
            time.sleep(delay)
            prevGamepadValues = gamepadValues
    except KeyboardInterrupt:
        print("Gamepad loop terminated...")
        pass

mcp3008.close()
print("MCP3008 connection terminated...")