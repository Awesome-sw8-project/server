docker swarm init --advertise-addr=127.0.0.1:52200
docker-compose build
docker stack deploy -c docker-compose.yml server