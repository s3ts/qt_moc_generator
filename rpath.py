#!/usr/bin/env python

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import argparse
import subprocess
import sys

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable",
                        help="The executable to add rpath to.")
    parser.add_argument("--rpath",
                        help="The rpath path to add to executable.")
    parser.add_argument("--touch",
                        help="The file to touch indicating success.")

    options = parser.parse_args()

    fullpath = '/usr/bin/install_name_tool' 
    assert fullpath
    
    executable = options.executable
    rpath = options.rpath
    touch = options.touch

    ret = subprocess.call([
        fullpath, '-add_rpath', rpath, executable
    ])
    if ret != 0:
        raise RuntimeError("Rpath has returned non-zero status: "
                           "{0} .".format(ret))
    if touch:
        ret = subprocess.call(['touch', touch])
    if ret != 0:
        raise RuntimeError("Rpath has returned non-zero status: "
                           "{0} .".format(ret))
    


if __name__ == "__main__":
    try:
        main(sys.argv)
    except RuntimeError as e:
        sys.exit(1)

