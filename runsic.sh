#!/bin/bash
source $(pwd)/venv/bin/activate
./sic.py $*
deactivate
