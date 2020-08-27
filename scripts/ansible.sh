#!/bin/sh
# make sure ~/.local/bin exists and is on your PATH
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
## install ansible with pip
pip install --user ansible
apt install pip
ansible-playbook -i inventory ansible/playbook.yaml