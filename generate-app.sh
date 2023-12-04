#!/usr/bin/env bash

export QT_MAC_WANTS_LAYER=1
cd "$(dirname $0)"
rm -rf build dist
python setup.py bdist_dmg
rm -rf build/dist build/exe.*

