#!/bin/sh
# make sure ~/.local/bin exists and is on your PATH
sudo mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
. ~/.bashrc
sudo apt install python3-pip
## install ansible with pip
pip3 install --user ansible

ansible-playbook -i inventory ansible/playbook.yaml