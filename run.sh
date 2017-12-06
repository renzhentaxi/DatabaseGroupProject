#! /usr/bin/env bash

./venv/bin/python ./Scripts/CSV/CleanCVS.py
./venv/bin/python ./Scripts/CSV/Excel2CSV.py

./venv/bin/python ./Scripts/Database/CleanDatabase.py
./venv/bin/python ./Scripts/Database/DatabaseInit.py
./venv/bin/python ./Scripts/Database/CSV2Database.py
