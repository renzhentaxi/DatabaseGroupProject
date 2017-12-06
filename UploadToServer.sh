#!/usr/bin/env bash

#clean everything on server
ssh renzhentaxibaerde@compsci.adelphi.edu "rm -r -f ~/*"
echo connect to server

scp  -r ~/PycharmProjects/DatabaseGroupProject/ renzhentaxibaerde@compsci.adelphi.edu:~/

echo upload complete