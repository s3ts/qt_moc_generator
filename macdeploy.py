#!/usr/bin/env python
#
# macdeploy.py
#
# Deploys plugins and qml imports for Mac App bundles.
#
# Copyright (c) Taehee Kim, 2017

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import argparse
import subprocess
import sys
import qt_shared

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable",
                        help="Allow executable to use deployed frameworks.")
    parser.add_argument("--qmldir",
                        help="Directory of QML files to use to determine which imports will be deployed.")
    parser.add_argument("--libpath",
                        help="Add given path to rpath.")
    parser.add_argument("--output",
                        help="Output bundle location.")
    parser.add_argument("--codesign",
                        help="Runs codesign with identity on all execs.")
    parser.add_argument("--touch",
                        help="The file to touch indicating success.")
    parser.add_argument("--always-overwrite",action="store_true", default=False,
                        help="Always overwrite the files.")
    parser.add_argument("--no-plugins",action="store_true", default=False,
                        help="Don't deploy plugins.")
    parser.add_argument("--no-strip",action="store_true", default=False,
                        help="Don't strip the executable.")
    parser.add_argument("--dmg",action="store_true", default=False,
                        help="Create dmg.")

    options = parser.parse_args()

    qt_shared.setupQTDIR()
    
    # MOC exists in the PATH
    fullpath = qt_shared.which('macdeployqt')
    assert fullpath

    args = []
    d = vars(options).iteritems()
    for k,v in d:
        if k in ["output", "touch"]:
            continue
        if k in ["always_overwrite", "no_plugins", "no_strip", "dmg"]:
            if not v:
                continue
            args.append("-" + k.replace('_', '-'))
            continue
        args.append("-" + k + "=" + v)
    
    assert options.output
    args.append(options.output)

    subprocArgs = [
        fullpath, 
        options.output,
        "-verbose=2"
    ] + args
    
    print(' '.join(subprocArgs))

    ret = subprocess.call([
        fullpath, 
        options.output,
        "-verbose=2"
    ] + args )
    if options.touch:
        ret = subprocess.call(['touch', options.touch])
    if ret != 0:
        raise RuntimeError("Macdeploy has returned non-zero status: "
                           "{0} .".format(ret))

if __name__ == "__main__":
    try:
        main(sys.argv)
    except RuntimeError as e:
        sys.exit(1)

