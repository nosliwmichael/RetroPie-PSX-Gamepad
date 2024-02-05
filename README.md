# MCP3008-Dual-Joystick
A Python script for reading button and joystick values in the Linux User-Space and translating them into inputs for a virtual gamepad.

This project was designed for a handheld RetroPie setup which uses an MCP3008 to handle Analog to Digital conversion and an MCP23017 for GPIO Expansion. The two chips combined can handle a total of 24 inputs (8 for the MCP3008 and 16 for the MCP23017). This does not include any available GPIO pins on the Raspberry Pi itself.

Input mappings for the gamepad can be configured with the gamepad.json file.

A complete list of the available gamepad inputs:
* Left Joystick
  * X-Axis
  * Y-Axis
  * Click
* Right Joystick
  * X-Axis
  * Y-Axis
  * Click
* D-PAD
  * UP
  * DOWN
  * LEFT
  * RIGHT
* ACTION
  * A
  * B
  * X
  * Y
* SHOULDER
  * LEFT BUMPER
  * RIGHT BUMPER
* TRIGGER
  * LEFT TRIGGER
  * RIGHT TRIGGER
* START
* SELECT
* HOME
* Not yet supported
  * POWER - Not yet 
  * VOLUME