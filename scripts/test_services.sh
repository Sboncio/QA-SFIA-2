#!/bin/bash
pip3 install -r ~/QA-SFIA-2/requirements.txt
cd ~/QA-SFIA-2/service1
/home/jenkins/.local/bin/pytest
cd ~/QA-SFIA-2/service2
/home/jenkins/.local/bin/pytest
cd ~/QA-SFIA-2/service3
/home/jenkins/.local/bin/pytest
cd ~/QA-SFIA-2/service4
/home/jenkins/.local/bin/pytest