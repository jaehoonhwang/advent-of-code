#!/usr/bin/sh

set -e

PROBLEM=$1

PYTHONPATH=. python answers/2019-answers.py $PROBLEM
