class SensorBase:
    def __init__(self):
        self.initialized = False
        self.sensor = None

        self.init_sensor()

    def init_sensor(self):
        pass

    def get_name(self):
        return None

    def get_data(self):
        return None
