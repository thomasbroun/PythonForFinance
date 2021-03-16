#!/bin/bash

git init
git add requirements.txt
mkdir test-env && cd test-env
python3 -m venv env
cd -
source env/bin/activate
pip3 install -r requirements.txt
python main.py

