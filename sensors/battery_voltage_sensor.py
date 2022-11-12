from sensors.sensor_base import SensorBase
from config import GPIOConfig
import machine
import utils


class BatteryVoltageSensor(SensorBase):
    def __init__(self):
        self.adc = None
        super().__init__()

    def get_name(self):
        return type(self).__name__

    def init_sensor(self):
        try:
            self.adc = machine.ADC(GPIOConfig.ADC_PIN)

            self.initialized = True

        except Exception as e:
            utils.print_debug(f"{self.get_name()}: {str(e)}")
            self.initialized = False

    def get_data(self):
        adc_value = self.adc.read_u16()
        adc_voltage = adc_value * GPIOConfig.ADC_CONVERSION_FACTOR

        voltage = adc_voltage * GPIOConfig.VOLTAGE_DIVIDER_FACTOR - GPIOConfig.ADC_ACCURACY

        data = {
            "battery_voltage": None
        }

        if self.initialized:
            data["battery_voltage"] = voltage

        return data
