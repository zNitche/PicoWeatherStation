import time
import machine
import utils
from config import GPIOConfig, APIConsts, CommonConfig
from controllers.sensors_controller import SensorsController
from controllers.network_controller import NetworkController


class Station:
    def __init__(self):
        self.onboard_led = machine.Pin("LED", machine.Pin.OUT)

        self.sensors_controller = SensorsController()
        self.network_controller = NetworkController()

        self.i2c = machine.I2C(0, scl=machine.Pin(GPIOConfig.SCL_PIN), sda=machine.Pin(GPIOConfig.SDA_PIN), freq=100000)

        self.toggle_onboard_led(True)

    def toggle_onboard_led(self, state):
        self.onboard_led.on() if state else self.onboard_led.off()

    def process(self):
        while True:
            try:
                self.network_controller.open_wlan_session()

                for sensor in self.sensors_controller.sensors:
                    sensor_data = sensor.get_data()
                    utils.print_debug(sensor_data)

                    for log_type, value in sensor_data.items():
                        data = {
                            APIConsts.API_VALUE_DATA_KEY: value
                        }

                        self.network_controller.send_post(f"{APIConsts.API_IP}{APIConsts.API_URL.format(log_type=log_type)}",
                                                          data,
                                                          {APIConsts.API_AUTH_TOKEN_KEY_NAME: APIConsts.API_AUTH_TOKEN})

            except Exception as e:
                utils.print_debug(str(e))

            finally:
                self.network_controller.close_wlan_session()

            time.sleep(CommonConfig.LOG_DELAY)

    def run(self):
        self.sensors_controller.init_sensors(self.i2c)
        self.process()
