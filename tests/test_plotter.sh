#!/usr/bin

set -u # error if variable unset
set -o # pipefail # fail if prior step failed

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

python -m unittest test_data_processor.py
pycodestyle $(git ls-files '*.py')

cd ..
run file_dimensions python data_processor.py get_file_dimensions 'iris.data'
assert_exit_code 0

run random_mat python data_processor.py get_random_matrix 2 1
assert_exit_code 0


