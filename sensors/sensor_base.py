class SensorBase:
    def __init__(self, i2c):
        self.initialized = False
        self.sensor = None
        self.i2c = i2c

        self.init_sensor()

    def init_sensor(self):
        pass

    def get_name(self):
        return None

    def get_data(self):
        return None
