# Estimation wrapper file.

# Entry estimation function.
# Argument data is of type Data.
def estimate(hybrid_method, data):
    bssids = data.get_antenna_data().get_bssids()
    rssi = list()
    imu = [data.get_imu_data().get_accelerometer(), data.get_imu_data().get_magnometer(), data.get_imu_data().get_gyroscope()]

    for bssid in bssids:
        rssi.extend(data.get_antenna_data().get_rssis(bssid))

    return hybrid_method.next_position(data.get_timestamp(), imu, rssi)
