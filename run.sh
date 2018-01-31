#!/bin/bash

find . -name '*.pyc' -delete
pytest tests
gunicorn -b 127.0.0.1:8038 --reload things.app
