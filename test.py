from evdev import UInput, AbsInfo, ecodes as e
from MCP3008 import MCP3008
from Joystick import Joystick
import time

# Instantiate MCP3008 class to assist with SPI communication to the MCP3008 chip
mcp3008 = MCP3008()

# Instantiate Joystick class to define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
left_joystick = Joystick()
right_joystick = Joystick(swt=3, vrx=4, vry=5)

# Define the capabilities of your virtual gamepad
cap = {
    e.EV_KEY : [0x13d, 0x13e],
    e.EV_ABS : [
        (e.ABS_X, AbsInfo(value=0, min=0, max=1000, fuzz=0, flat=0, resolution=0)),
        (e.ABS_Y, AbsInfo(0, 0, 1000, 0, 0, 0)),
        (e.ABS_RX, AbsInfo(0, 0, 1000, 0, 0, 0)),
        (e.ABS_RY, AbsInfo(0, 0, 1000, 0, 0, 0))
    ]
}

def convertBtnValue(btnVal):
    return 1 if btnVal < 500 else 0

def readChannel(adcChannel):
    return mcp3008.read(adcChannel.channel)

def updateJoystickValues(joystick):
    joystick.swtValue = convertBtnValue(readChannel(joystick.swtChannel))
    joystick.vryValue = readChannel(joystick.vryChannel)
    joystick.vrxValue = readChannel(joystick.vrxChannel)

mcp3008.open()
# Create a virtual input device
with UInput(cap, name='example-device', version=0x3) as ui:
    for x in range(0, 800):
        ui.write(e.EV_ABS, x, 1000)
        ui.syn()
        time.sleep(0.05)
        print(x)
#     while True:
#         # Read joystick values
#         updateJoystickValues(left_joystick)
#         updateJoystickValues(right_joystick)
#         lx = left_joystick.vrxValue
#         ly = left_joystick.vryValue
#         lz = left_joystick.swtValue
#         rx = right_joystick.vrxValue
#         ry = right_joystick.vryValue
#         rz = right_joystick.swtValue
# 
#         # Emit joystick events
#         ui.write(e.EV_ABS, e.ABS_X, lx)
#         ui.write(e.EV_ABS, e.ABS_Y, ly)
#         ui.write(e.EV_ABS, e.ABS_RX, rx)
#         ui.write(e.EV_ABS, e.ABS_RY, ry)
#         
#         # Emit button events
#         ui.write(e.EV_KEY, 317, lz)
#         ui.write(e.EV_KEY, 318, rz)
# 
#         # Synchronize events
#         ui.syn()
# 
#         # Delay to prevent excessive CPU usage
#         time.sleep(0.01)
