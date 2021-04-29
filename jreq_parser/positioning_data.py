# Abstract class for representing data.
class DataSource:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

# Class of IMU data.
class IMU(DataSource):
    def __init__(self, accelerometer, gyroscope, magnometer):
        super().__init__([accelerometer, gyroscope, magnometer])
        self.acc = accelerometer
        self.gyr = gyroscope
        self.mag = magnometer

    def get_accelerometer(self):
        return self.acc

    def get_gyroscope(self):
        return self.gyr

    def get_magnometer(self):
        return self.mag

# Class of antenna data.
class Antenna(DataSource):
    def __init__(self, data_map):
        super().__init__(data_map)
        self.map = data_map

    # Returns list of BSSIDs.
    def get_bssids(self):
        return list(self.map.keys())

    # Returns RSSIs from given BSSID.
    def get_rssis(self, bssid):
        return self.map[bssid]