# Indoor Positioning Server
This is our solution server for indoor positioning estimations.

## Setup
Initialize the swarm running the command:

`docker swarm init --advertise-addr=<IP ADDRESS>:52200`

Usually, local IP address can be used for local testing.
Then, build and deploy Docker Compose with the following commands:

````
docker-compose build
docker stack deploy -c docker-compose.yml server
````

## Usage
Clients send a JSON object with measurements and get a response back with the position estimation. The transmission of these JSON objects happen using HHTP GET-requests. The JSON obejct format is as specified below:

````
{
  "timestamp": <TIMESTAMP>,
  "is_bluetooth": <BOOL>1,
  "is_wifi": <BOOL2>,
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
  "antenna": [<V1>, <V2>, ..., <VN>]
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
