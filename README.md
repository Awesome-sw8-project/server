# Indoor Positioning Server
![Tests](https://github.com/Awesome-sw8-project/server/actions/workflows/python-app.yml/badge.svg)

This is our solution server for indoor positioning estimations.

## Setup
Add the hybrid estimator by changing to directory `estimator`.
Clone the `experiments` repository running the following command:

````
git clone https://github.com/Awesome-sw8-project/experiments.git
````

Initialize the swarm running the command from the root directory:

````
docker swarm init --advertise-addr=<IP ADDRESS>:52200
````

Usually, local IP address can be used for local testing.
Then, build and deploy Docker Compose with the following commands:

````
docker-compose build
docker stack deploy -c docker-compose.yml server
````

## Usage
Clients send a JSON array of JSON objects with measurements and get a response back with the position estimation. The transmission of these JSON objects happen using HTTP POST-requests. A JSON array element is as specified below:

````
{
  "timestamp": <TIMESTAMP>,
  "is_bluetooth": <BOOL1>,
  "is_wifi": <BOOL2>,
  "start": {
    "x": <X0>,
    "y": <Y0>,
    "z": <Z0>
  }
  "IMU": {
    "accelerometer": {
      "x": <X1>,
      "y": <Y1>,
      "z": <Z1>
    },
    "gyroscope": {
      "x": <X2>,
      "y": <Y2>,
      "z": <Z2>
    },
    "magnometer": {
      "x": <X3>,
      "y": <Y3>,
      "z": <Z3>
    }
  },
  "antenna": [
    {
      "bssid": <BSSID1>,
      "rssi": [<RSSI11>, <RSSI12>, ..., <RSSI1N>]
    },
    {
      "bssid": <BSSID2>,
      "rssi": [<RSSI21>, <RSSI22>, ..., <RSSI2N>]
    },
    ...
    {
      "bssid": <BSSID3>,
      "rssi": [<RSSI31>, <RSSI32>, ..., <RSSI3N>]
    }
  ]
}
````

The response will be on the following format:


````
{
  "x": <X>,
  "y": <Y>,
  "z": <Z>
}
````
