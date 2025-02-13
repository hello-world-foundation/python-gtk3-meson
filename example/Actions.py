#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys

def usage():
    print("Usage ./Actions.py ...")

def hello():
    subprocess.run(["echo", "Hello World"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    if sys.argv[1] == "hello":
        hello()