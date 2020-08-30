#!/bin/bash
DIR="./artifacts"
cd ~
if [ -d "$DIR" ]; then
    rm -r ~/artifacts
    mkdir ~/artifacts
    sudo docker save service1 service2 service3 service4 > ~/artifacts/artifact.tar
else
    echo "doesn't exist"
    mkdir ~/artifacts
    sudo docker save service1 service2 service3 service4 > ~/artifacts/artifact.tar
fi