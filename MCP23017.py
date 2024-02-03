#!/usr/bin/env python3

import smbus
import time

DEVICE = 0x20 # Device address of MCP23017
IODIRA = 0x00 # Input/Output Direction Port A
IODIRB = 0x01 # Input/Output Direction Port B
GPPUA = 0x0C # Pull-Up Resistory Registry for Port A
GPPUB = 0x0D # Pull-Up Resistory Registry for Port B
GPIOA = 0x12 # Input Registry for Port A
GPIOB = 0x13 # Input Registry for Port B
OLATA = 0x14 # Output Registry for Port A
OLATB = 0x15 # Output Registry for Port B

class MCP23017:
    def __init__(self):
        # Raspberry Pi 4 uses bus 1 for I2C
        self.bus = smbus.SMBus(1)
        
        # Setup pins as input
        self.bus.write_byte_data(DEVICE, IODIRA, 0xFF)
        self.bus.write_byte_data(DEVICE, IODIRB, 0xFF)

        # Enable pull-up resistors
        self.bus.write_byte_data(DEVICE, GPPUA, 0xFF)
        self.bus.write_byte_data(DEVICE, GPPUB, 0xFF)
    
    def readGPIO(self, port, mask):
        registry = GPIOA
        if (port == "B"):
            registry = GPIOB
        
        byte_value = self.bus.read_byte_data(DEVICE, registry)

        return 1 if byte_value & mask == 0b0 else 0