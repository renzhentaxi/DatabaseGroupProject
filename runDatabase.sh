#! /usr/bin/env bash


python2 ./Scripts/Database/CleanDatabase.py
python2 ./Scripts/Database/DatabaseInit.py
python2 ./Scripts/Database/CSV2Database.py
