#!/bin/bash

make clean
make html
python -m http.server 7000 -d _build/html/
