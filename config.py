class CommonConfig:
    DEBUG_MODE = False
    LOG_DELAY = 1800


class APIConsts:
    API_AUTH_TOKEN_KEY_NAME = "auth_token"
    API_AUTH_TOKEN = "" #WeatherStationAPI auth key
    API_VALUE_DATA_KEY = "value"
    API_IP = "" #WeatherStationAPI IP address
    API_URL = "/api/logs/{log_type}/add"


class NetworkConfig:
    MAX_WIFI_RECONNECT_ATTEMPTS = 3

    WIFI_SSID = ""
    WIFI_PASSWORD = ""


class GPIOConfig:
    AHT20_I2C_ADDRESS = 0x38
    SCL_PIN = 9
    SDA_PIN = 8
    ADC_PIN = 28

    ADC_CONVERSION_FACTOR = 3.3 / 65476
    VOLTAGE_DIVIDER_FACTOR = 2  # 1V ON ADC PIN = 2V OF SOURCE VOLTAGE
    ADC_ACCURACY = 0.05
