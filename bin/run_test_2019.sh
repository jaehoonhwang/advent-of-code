#!/bin/sh

set -e

PROBLEM=$1
OS="`uname`"

if (( $OS == Darwin))
then
    echo "DETECTED OSX"
    PYTHONPATH=. python3 answers/2019-answers.py $PROBLEM
    exit 0
fi

PYTHONPATH=. python answers/2019-answers.py $PROBLEM
