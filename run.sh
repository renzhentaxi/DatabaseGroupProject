#! /usr/bin/env bash

python3 ./Scripts/CSV/CleanCVS.py
python3 ./Scripts/CSV/Excel2CSV.py

python3 ./Scripts/Database/CleanDatabase.py
python3 ./Scripts/Database/DatabaseInit.py
python3 ./Scripts/Database/CSV2Database.py
