#!/bin/bash

if [[ $# == 1 ]] && [[ $1 != "help" ]]
then
    python3 main.py $1

elif [[ $# == 1 ]] && [[ $1 == "help" ]]
then 
    cat start_help.txt

else
    cat start_help.txt

fi
