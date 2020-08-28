#!/bin/bash
# make sure ~/.local/bin exists and is on your PATH
sudo mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
sudo source ~/.bashrc
sudo apt install pip
## install ansible with pip
pip install --user ansible

ansible-playbook -i inventory ansible/playbook.yaml