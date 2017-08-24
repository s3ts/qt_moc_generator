#!/usr/bin/env python
#
# qt_moc_generator.py
#
# This script takes the qrc files and uses the Qt RCC to generate the source file for resources.
# The output files will be named: {rcc file}.qrc.cc
#
# Copyright (c) Taehee Kim, 2017

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import argparse
import subprocess
import sys
import shared

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        help="The .qrc file.")
    parser.add_argument("--output",
                        help="The fullpath of the output file.")

    options = parser.parse_args()

    shared.setupQTDIR()
    
    # MOC exists in the PATH
    fullpath = shared.which('rcc')
    assert fullpath
    
    input = options.input
    output = options.output

    ret = subprocess.call([
        fullpath, 
        input,
        "-o", output 
    ])
    if ret != 0:
        raise RuntimeError("Rcc has returned non-zero status: "
                           "{0} .".format(ret))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except RuntimeError as e:
        sys.exit(1)

