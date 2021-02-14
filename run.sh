#!/bin/bash

git init
git add requirements.txt
mkdir test-env && cd test-env
python3 -m venv env
cd -
source env/bin/activate
python main.py

