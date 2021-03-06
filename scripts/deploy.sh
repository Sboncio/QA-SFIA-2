#!/bin/sh
echo ${DATABASE_URI}
echo ${SECRET_KEY_DB}
python3 ./scripts/test.py
sudo docker-compose build
sudo docker-compose push
sudo docker stack deploy --compose-file docker-compose.yaml sfia2
sudo docker service scale sfia2_service1=3 sfia2_service2=3 sfia2_service3=3 sfia2_service4=3
sudo docker service update --image sboncio/service1 sfia2_service1