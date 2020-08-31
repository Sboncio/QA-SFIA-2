#!/bin/bash
pip3 install -r ./requirements.txt
cd ./service1
/home/jenkins/.local/bin/pytest --cov-report html
cd ../service2
/home/jenkins/.local/bin/pytest --cov-report html
cd ../service3
/home/jenkins/.local/bin/pytest --cov-report html
cd ../service4
/home/jenkins/.local/bin/pytest --cov-report html