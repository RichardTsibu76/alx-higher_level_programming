#!/bin/bash
echo "Compiling main.py ..." && python3 -m py_compile $PYFILE && mv __pycache__/*.pyc "$PYFILE"c  && rm -rf __pycache__
