#!/bin/bash
virtualenv -q -p /usr/bin/python3.5 $1
source $1/bin/activate
pip install -r requirements.txt