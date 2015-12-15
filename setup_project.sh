#!/usr/bin/env bash

set -e

virtualenv --python=python3.4 venv
source venv/bin/activate && pip install -r requirements.txt