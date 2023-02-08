#!/bin/sh

# To make this script usable, you may have to run chmod u+x callPython.sh first
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        python ./updateGoogleDNS.py
elif [[ "$OSTYPE" == "darwin"* ]]; then
        python3 ./updateGoogleDNS.py
fi