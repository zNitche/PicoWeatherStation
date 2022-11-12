from sensors.sensor_base import SensorBase
from libs.aht20 import AHT20
from config import GPIOConfig
import utils


class AHT20Sensor(SensorBase):
    def __init__(self, i2c):
        self.i2c = i2c

        super().__init__()

    def init_sensor(self):
        try:
            self.sensor = AHT20(self.i2c, address=GPIOConfig.AHT20_I2C_ADDRESS)

            self.initialized = True

        except Exception as e:
            utils.print_debug(f"{self.get_name()}: {str(e)}")
            self.initialized = False

    def get_name(self):
        return type(self).__name__

    def get_data(self):
        data = {
            "temperature": None,
            "humidity": None
        }

        if self.initialized:
            data["temperature"] = self.sensor.get_temperature()
            data["humidity"] = self.sensor.get_relative_humidity()

        return data
