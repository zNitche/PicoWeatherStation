import time
import machine
from libs import aht20
from consts import Consts


class Station:
    def __init__(self):
        self.onboard_led = machine.Pin("LED", machine.Pin.OUT)
        self.i2c = machine.I2C(0, scl=machine.Pin(Consts.SCL_PIN), sda=machine.Pin(Consts.SDA_PIN), freq=100000)

        self.temp_sensor = None
        self.display = None

        self.initialized = False

    def init_sensor(self):
        try:
            self.temp_sensor = aht20.AHT20(self.i2c, address=Consts.AHT20_I2C_ADDRESS)

            self.initialized = True

        except Exception as e:
            self.initialized = False

    def process(self):
        while True:
            if self.initialized:
                temp = self.temp_sensor.get_temperature()
                hum = self.temp_sensor.get_relative_humidity()

                print(f"Temp: {temp}, Hum: {hum}")

            else:
                self.onboard_led.toggle()

            time.sleep(1)

    def run(self):
        self.init_sensor()
        self.process()
