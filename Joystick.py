from ADCChannel import ADCChannel

class Joystick:
    def __init__(self, swt = 0, vrx = 1, vry = 2):
        self.swtChannel = ADCChannel(swt, 0)
        self.vrxChannel = ADCChannel(vrx, 0)
        self.vryChannel = ADCChannel(vry, 0)
    
    @property
    def swtValue(self):
        return self.swtChannel.value
    
    @swtValue.setter
    def swtValue(self, value):
        self.swtChannel.value = value
    
    @property
    def vrxValue(self):
        return self.vrxChannel.value
    
    @vrxValue.setter
    def vrxValue(self, value):
        self.vrxChannel.value = value
    
    @property
    def vryValue(self):
        return self.vryChannel.value
    
    @vryValue.setter
    def vryValue(self, value):
        self.vryChannel.value = value