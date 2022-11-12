import network
import time
from config import NetworkConfig
import utils
import urequests
import json


class NetworkController:
    def __init__(self):
        self.wlan = self.init_wlan()

    def init_wlan(self):
        utils.print_debug("WLAN init...")
        wlan = network.WLAN(network.STA_IF)

        return wlan

    def toggle_wlan(self, status):
        if not status == self.wlan.active():
            self.wlan.active(status)

        utils.print_debug(f"WLAN Status: {self.wlan.active()}")

    def check_if_wlan_enabled(self):
        return self.wlan.active()

    def activate_wlan_if_disabled(self):
        if not self.wlan.active():
            utils.print_debug("Enabling WLAN interface...")

            self.toggle_wlan(True)

    def connect_to_network(self, ssid, password):
        self.activate_wlan_if_disabled()

        utils.print_debug("Connecting to WIFI network...")

        self.network_connection_loop(ssid, password)

        if self.wlan.isconnected():
            utils.print_debug(f"Connected to '{ssid}' network...")
            utils.print_debug(f"IP address: {self.wlan.ifconfig()[0]}...")

        else:
            utils.print_debug("Failed to connect...")

    def network_connection_loop(self, ssid, password):
        attempts = 0

        while (not self.wlan.isconnected()) and attempts < NetworkConfig.MAX_WIFI_RECONNECT_ATTEMPTS:
            utils.print_debug("Trying to establish WiFi connection...")

            time.sleep(5)
            self.wlan.connect(ssid, password)

            attempts += 1

    def disconnect_from_network(self):
        utils.print_debug("Disconnecting from network...")

        if self.wlan.isconnected():
            self.wlan.disconnect()

    def get_wlan_config(self):
        config = None

        if self.wlan.active() and self.wlan.isconnected():
            config = self.wlan.ifconfig()

        return config

    def get_wifi_networks(self):
        utils.print_debug("Getting wifi networks...")
        self.activate_wlan_if_disabled()

        networks = self.wlan.scan()

        return networks

    def send_post(self, url, payload, headers):
        response = urequests.post(url, data=json.dumps(payload), headers=headers, timeout=2)
        response.close()

    def open_wlan_session(self):
        self.toggle_wlan(True)
        self.connect_to_network(NetworkConfig.WIFI_SSID, NetworkConfig.WIFI_PASSWORD)

    def close_wlan_session(self):
        self.disconnect_from_network()
        self.toggle_wlan(False)
