#!/usr/bin

set -u # error if variable unset
set -o # pipefail # fail if prior step failed

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

python -m unittest test_data_processor.py
pycodestyle $(git ls-files '*.py')