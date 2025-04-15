#!/bin/sh
pipenv sync -d
pipenv run python main.py -gui
