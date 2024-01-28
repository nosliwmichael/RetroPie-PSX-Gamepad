# MCP3008-Dual-Joystick
A Python script to handle two joystick inputs through an MCP3008

The MCP3008 class was pulled from tutorials-raspberrypi.com in a guide showing how to use the MCP3008 with the Raspberry Pi. Using SpiDev, it provides a default bus and chip select value which is suitable for this project since we only have one SPI device.