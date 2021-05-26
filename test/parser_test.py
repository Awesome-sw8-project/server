import sys
sys.path.append(".")
import jreq_parser.req_parser as rp

# Tests parsing of single-element JSON array.
def test_single_json():
    j_str = """[{\"timestamp\": 1,
                 \"is_bluetooth\": true,
                 \"is_wifi\": false,
                 \"start\": {
                     \"x\": 1,
                     \"y\": 2,
                     \"z\": 3
                 },
                 \"IMU\": {
                     \"accelerometer\": {
                         \"x\": 1,
                         \"y\": 2,
                         \"z\": 3
                     },
                     \"gyroscope\": {
                         \"x\": 4,
                         \"y\": 5,
                         \"z\": 6
                     },
                     \"magnometer\": {
                         \"x\": 7,
                         \"y\": 8,
                         \"z\": 9
                     }
                 },
                 \"antenna\": [
                     {
                         \"bssid\": 12345,
                         \"rssi\": [10, 20, 30]
                     },
                     {
                         \"bssid\": 12345,
                         \"rssi\": [10, 20, 30]
                     }
                 ]
             }]"""

    data = rp.parse_json(j_str)
    assert(len(data) == 1)

    data = data[0]
    assert(data.is_bluetooth())
    assert(not data.is_wifi())
    assert(data.get_timestamp() == 1)

    imu = data.get_imu_data()
    antenna = data.get_antenna_data()
    assert(imu.get_accelerometer() == [1, 2, 3])
    assert(imu.get_gyroscope() == [4, 5, 6])
    assert(imu.get_magnometer() == [7, 8, 9])
    assert(antenna.get_bssids() == [12345])
    assert(antenna.get_rssis(12345) == [10, 20, 30])

# Tests parsing of multi-element JSON array.
def test_multi_json():
    j_str = """[{\"timestamp\": 1,
                 \"is_bluetooth\": true,
                 \"is_wifi\": false,
                 \"start\": {
                     \"x\": 10,
                     \"y\": 20,
                     \"z\": 30
                 },
                 \"IMU\": {
                     \"accelerometer\": {
                     \"x\": 1,
                     \"y\": 2,
                     \"z\": 3
                 },
                 \"gyroscope\": {
                     \"x\": 4,
                     \"y\": 5,
                     \"z\": 6
                 },
                 \"magnometer\": {
                     \"x\": 7,
                     \"y\": 8,
                     \"z\": 9
                 }
             },
             \"antenna\": [
                 {
                     \"bssid\": 12345,
                     \"rssi\": [10, 20, 30]
                 },
                 {
                     \"bssid\": 56789,
                     \"rssi\": [20, 40, 60]
                 }
             ]
         },
         {
             \"timestamp\": 2,
             \"is_bluetooth\": true,
             \"is_wifi\": false,
             \"start\": {
                 \"x\": 10,
                 \"y\": 5,
                 \"z\": 15
             },
             \"IMU\": {
                 \"accelerometer\": {
                     \"x\": 5,
                     \"y\": 6,
                     \"z\": 3
                 },
                 \"gyroscope\": {
                     \"x\": 9,
                     \"y\": 8,
                     \"z\": 7
                 },
                 \"magnometer\": {
                     \"x\": 3,
                     \"y\": 3,
                     \"z\": 3
                 }
             },
             \"antenna\": [
                 {
                     \"bssid\": 59372,
                     \"rssi\": [80, 60, 40]
                 },
                 {
                     \"bssid\": 44553,
                     \"rssi\": [50, 60, 40]
                 }
            ]}]"""

    data = rp.parse_json(j_str)
    data1 = data[0]
    data2 = data[1]
    assert(len(data) == 2)

    assert(data1.is_bluetooth() and data2.is_bluetooth())
    assert(not data1.is_wifi() and not data2.is_wifi())
    assert(data1.get_timestamp() == 1)
    assert(data2.get_timestamp() == 2)

    assert(data1.get_imu_data().get_accelerometer() == [1, 2, 3])
    assert(data1.get_imu_data().get_gyroscope() == [4, 5, 6])
    assert(data1.get_imu_data().get_magnometer() == [7, 8, 9])
    assert(data2.get_imu_data().get_accelerometer() == [5, 6, 3])
    assert(data2.get_imu_data().get_gyroscope() == [9, 8, 7])
    assert(data2.get_imu_data().get_magnometer() == [3, 3, 3])

    assert(data1.get_antenna_data().get_bssids() == [12345, 56789])
    assert(data2.get_antenna_data().get_bssids() == [59372, 44553])
    assert(data1.get_antenna_data().get_rssis(12345) == [10, 20, 30])
    assert(data1.get_antenna_data().get_rssis(56789) == [20, 40, 60])
    assert(data2.get_antenna_data().get_rssis(59372) == [80, 60, 40])
    assert(data2.get_antenna_data().get_rssis(44553) == [50, 60, 40])

test_single_json()
