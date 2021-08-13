import adafruit_max31865
import busio
import digitalio

import constants


class Temp_Probe:
    def __init__(self, sck, mosi, miso, cs, wires=2):
        self.spi = busio.SPI(sck, MOSI=mosi, MISO=miso)
        self.cs = digitalio.DigitalInOut(cs)
        self.sensor = adafruit_max31865.MAX31865(
            self.spi,
            self.cs,
            wires=wires,
            rtd_nominal=constants.TEMP_NOMINAL_RESISTANCE,
            ref_resistor=constants.TEMP_REF_RESISTANCE,
        )

    def get_temperature(self):
        return self.sensor.temperature

    def get_resistance(self):
        return self.sensor.resistance
