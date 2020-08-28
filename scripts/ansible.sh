#!/bin/bash
# make sure ~/.local/bin exists and is on your PATH
sudo mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
. ~/.bashrc
sudo apt install python3-pip
## install ansible with pip
sudo pip3 install ansible
#sudo apt install ansible
ansible-playbook -i ./ansible/inventory ./ansible/playbook.yaml