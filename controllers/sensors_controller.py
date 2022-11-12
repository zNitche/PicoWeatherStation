from sensors.aht20_sensor import AHT20Sensor
from sensors.battery_voltage_sensor import BatteryVoltageSensor


class SensorsController:
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def init_sensors(self, i2c):
        self.sensors.append(AHT20Sensor(i2c))
        self.sensors.append(BatteryVoltageSensor())

    def get_sensor_by_name(self, sensor_name):
        f_sensor = None

        for sensor in self.sensors:
            if sensor.get_name() == sensor_name:
                f_sensor = sensor
                break

        return f_sensor
