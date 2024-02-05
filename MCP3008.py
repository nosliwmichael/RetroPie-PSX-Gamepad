#!/usr/bin/python
# ==============================
# https://tutorials-raspberrypi.com/mcp3008-read-out-analog-signals-on-the-raspberry-pi/#google_vignette
# ==============================
from spidev import SpiDev
 
class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
    
    def __enter__(self):
        self.spi.open(self.bus, self.device)
        self.spi.max_speed_hz = 1000000 # 1MHz
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spi.close()

    def read(self, channel = 0):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data