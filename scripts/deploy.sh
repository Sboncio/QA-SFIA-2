#!/bin/sh
sudo docker-compose build
sudo docker stack deploy --compose-file docker-compose.yaml sfia2
sudo docker service scale service1=3 service2=3 service3=3 service4=3