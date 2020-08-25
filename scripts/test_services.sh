#!/bin/bash
echo $(pwd)
cd ~/QA-SFIA-2/service1
/home/jenkins/.local/bin/pytest
cd ~/QA-SFIA-2/service2
/home/jenkins/.local/bin/pytest
cd ~/QA-SFIA-2/service3
/home/jenkins/.local/bin/pytest
cd ~/QA-SFIA-2/service4
/home/jenkins/.local/bin/pytest