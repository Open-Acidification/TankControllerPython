#!/bin/sh
pipenv sync -d
pipenv run pytest -vv
