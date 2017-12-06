#! /usr/bin/env bash

source ./venv/bin/activate

python ./Scripts/Database/CleanDatabase.py
python ./Scripts/Database/DatabaseInit.py
python ./Scripts/Database/CSV2Database.py
