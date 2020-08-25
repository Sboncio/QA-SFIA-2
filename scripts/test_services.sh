#!/bin/bash
echo $(pwd)
cd service1
pytest
cd service2
pytest
cd service3
pytest
cd service4
pytest