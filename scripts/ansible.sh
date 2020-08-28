#!/bin/bash
# make sure ~/.local/bin exists and is on your PATH
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
apt install pip
## install ansible with pip
pip install --user ansible

ansible-playbook -i inventory ansible/playbook.yaml