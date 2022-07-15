#!/bin/bash

if [[ $# == 1 ]]
then
    python3 main.py $1
else
    echo "Error:
    Please provide ONLY your first name after ./startapp.sh, For example, ./startapp.sh NAME" >&2
fi
