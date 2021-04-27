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
To be finished...
