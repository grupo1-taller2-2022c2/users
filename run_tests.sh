#!/bin/bash

#coverage run -m pytest && coverage report -m
pytest
pytest --cache-clear --cov=app tests/ --cov-report=xml > pytest-coverage.txt
echo "Listo"