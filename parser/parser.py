# Parser module of JSON object containing Wi-Fi data and IMU data.

import positioning_data as pd
import json

# Class representing parsed JSON object data.
class Data:
    def __init__(self, timestamp, is_bluetooth, is_wifi, imu, antenna):
        self.timestamp = timestamp
        self.bluetooth = is_bluetooth
        self.wifi = is_wifi
        self.imu = imu
        self.antenna = antenna

    # Getter methods.
    def get_timestamp(self):
        return self.timestamp

    def is_bluetooth(self):
        return self.bluetooth

    def is_wifi(self):
        return self.wifi

    def get_imu_data(self):
        return self.imu
    
    def get_antenna_data(self):
        return self.antenna

# Main entry for parsing JSON object string.
def parse_json(str):
    obj = json.loads(str)
    acc = obj["IMU"]["accelerometer"]
    gyr = obj["IMU"]["gyroscope"]
    mag = obj["IMU"]["magnometer"]
    antenna_data = dict()

    for antenna in obj["antenna"]:
        antenna_data[antenna["bssid"]] = antenna["rssi"]

    imu = pd.IMU([acc["x"], acc["y"], acc["z"]], [gyr["x"], gyr["y"], gyr["z"]], [mag["x"], mag["y"], mag["z"]])
    antenna = pd.Antenna(antenna_data)

    return Data(obj["timestamp"], obj["is_bluetooth"], obj["is_wifi"], imu, antenna)