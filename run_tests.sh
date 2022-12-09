#!/bin/bash

#coverage run -m pytest && coverage report -m
pytest --cache-clear --cov=app --cov-report=xml > pytest-coverage.txt