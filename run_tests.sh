#!/bin/bash

#coverage run -m pytest && coverage report -m
pytest
pytest --cache-clear --cov=app --cov-report=xml > pytest-coverage.txt