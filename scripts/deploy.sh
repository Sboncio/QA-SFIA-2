#!/bin/sh
sudo docker-compose build
sudo docker stack deploy --compose-file docker-compose.yaml sfia2
sudo docker service scale sfia2_service1=3 sfia2_service2=3 sfia2_service3=3 sfia2_service4=3