#!/bin/bash
echo $(pwd)
cd ~/QA-SFIA-2/service1
pytest
cd ~/QA-SFIA-2/service2
pytest
cd ~/QA-SFIA-2/service3
pytest
cd ~/QA-SFIA-2/service4
pytest