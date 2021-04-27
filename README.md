# Indoor Positioning Server
This is our solution server for indoor positioning estimations.

## Setup
Initialize the swarm running the command:

`docker swarm init --advertise-addr=127.0.0.1:52200`

Then, build and deploy Docker compose with the following commands:

````
docker-compose build
docker stack deploy -c docker-compose.yml server
````

## Usage
To be finished...
