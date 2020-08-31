#!/bin/bash
DIR="./artifacts"
cd ~
if [ -d "$DIR" ]; then
    rm -r ~/artifacts
    mkdir ~/artifacts
    sudo docker save sboncio/service1 sboncio/service2 sboncio/service3 sboncio/service4 > ~/artifacts/artifact.tar
else
    echo "doesn't exist"
    mkdir ~/artifacts
    sudo docker save sboncio/service1 sboncio/service2 sboncio/service3 sboncio/service4 > ~/artifacts/artifact.tar
fi