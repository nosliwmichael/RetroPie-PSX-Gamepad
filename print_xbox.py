from evdev import InputDevice, categorize, ecodes

# Find your device file path in /dev/input/ by listing all devices and identifying your controller
gamepad = InputDevice('/dev/input/event4')  # Replace 'eventX' with the correct event number for your Xbox controller

print(f"Reading from: {gamepad.name}")
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))  # Prints button presses
    elif event.type in [ecodes.EV_ABS]:
        absevent = categorize(event)
        #print(ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)
