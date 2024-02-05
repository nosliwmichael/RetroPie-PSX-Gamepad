#!/usr/bin/env python3

from smbus2 import SMBus
import time

# This is the address of the MCP23017 when pins A0-A2 are pulled to Ground
DEVICE = 0x20 # Device address of MCP23017

# These are the register addresses for IOCON.BANK=0
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
        self.bus = SMBus(1)
        
        # Setup pins as input
        self.bus.write_byte_data(DEVICE, IODIRA, 0xFF)
        self.bus.write_byte_data(DEVICE, IODIRB, 0xFF)

        # Enable pull-up resistors
        self.bus.write_byte_data(DEVICE, GPPUA, 0xFF)
        self.bus.write_byte_data(DEVICE, GPPUB, 0xFF)
        print("Initialized the SMBus...")
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.bus.close()
    
    def readGPIO(self, port: str):
        """
        This method reads all GPIO pins for the given port on the MCP23017.

        :param port: The MCP23017 chip has 16 total GPIO pins that are divided
            between two 8-bit ports (PORTA and PORTB)
            More information can be found in section "3.0 Device Overview" of the datasheet.
            https://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf
        :type port: str "A" or "B"
        """
        registry = GPIOA
        if (port == "B"):
            registry = GPIOB
        
        bits = list(bin(self.bus.read_byte_data(DEVICE, registry))[2:])
        
        return bits