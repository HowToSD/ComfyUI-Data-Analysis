#!/bin/bash
# Run this command on project root
# ```
# dev/scripts/run_tests.sh
# ````
# If you add a new test file, make sure that the directory contains an empty
# __init__.py. Otherwise, unittest won't be able to find the directory and
# the tests in the directory will be skipped.
export PYTHONPATH=modules:$PYTHONPATH
echo $PYTHONPATH
RUN_SKIPPED_TESTS=0 python -m unittest discover -s tests -p "*_test.py" -t .

