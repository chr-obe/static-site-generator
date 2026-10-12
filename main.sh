#!/bin/bash

# start the static site generator
python3 src/main.py

# open it as a website on port 8888
cd public && python3 -m http.server 8888
