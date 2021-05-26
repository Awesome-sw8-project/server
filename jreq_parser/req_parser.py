# Parser module of JSON object containing Wi-Fi data and IMU data.

from jreq_parser import positioning_data as pd
import json

# Class representing parsed JSON object data.
class Data:
    def __init__(self, timestamp, is_bluetooth, is_wifi, start_location, imu, antenna):
        self.timestamp = timestamp
        self.bluetooth = is_bluetooth
        self.wifi = is_wifi
        self.imu = imu
        self.antenna = antenna
        self.start = start_location

    # Getter methods.
    def get_timestamp(self):
        return self.timestamp

    def is_bluetooth(self):
        return self.bluetooth

    def is_wifi(self):
        return self.wifi

    def get_start_location(self):
        return self.start

    def get_imu_data(self):
        return self.imu

    def get_antenna_data(self):
        return self.antenna

# Main entry for parsing JSON object string.
# Returns list of Data instances.
def parse_json(str):
    obj = json.loads(str)
    data_list = []

    for element in obj:
        antenna_data = dict()
        acc = element["IMU"]["accelerometer"]
        gyr = element["IMU"]["gyroscope"]
        mag = element["IMU"]["magnometer"]
        start = [element["start"]["x"], element["start"]["y"], element["start"]["z"]]

        for antenna in element["antenna"]:
            antenna_data[antenna["bssid"]] = antenna["rssi"]

        imu = pd.IMU([acc["x"], acc["y"], acc["z"]], [gyr["x"], gyr["y"], gyr["z"]], [mag["x"], mag["y"], mag["z"]])
        antenna = pd.Antenna(antenna_data)
        data_list.append(Data(element["timestamp"], element["is_bluetooth"], element["is_wifi"], start, imu, antenna))

    return data_list
