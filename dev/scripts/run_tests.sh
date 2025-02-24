#!/bin/bash
# Run this command on project root
# ```
# dev/scripts/run_tests.sh
# ````
export PYTHONPATH=modules:$PYTHONPATH
echo $PYTHONPATH
python -m unittest discover -s tests -p "*_test.py" -t .

