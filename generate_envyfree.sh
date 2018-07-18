#!/bin/bash
# until (python3 generate_hr_test.py |  python3 roth_peranson_matching.py > roth_output.txt; cat roth_output.txt) | grep -m 1 "ENVY FREE TRUE"; do : ; done
until (python3 generate_hr_test.py |  python3 roth_peranson_matching.py ) | grep -m 1 "ENVY FREE TRUE"; do : ; done