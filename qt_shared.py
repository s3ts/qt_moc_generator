
#!/usr/bin/env python
#
# qt_moc_generator.py
#
# This script takes the header files and uses the Qt MOC to generate the Meta-Object source.
# The output files will be named: {header file name}.moc.cc
#
# Copyright (c) Taehee Kim, 2017

import os
import os.path

# From https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
    
    if os.name == 'nt':
        program += '.exe'

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

# If QTDIR is in the environment, prefer using QTDIR so prepend to PATH.
def setupQTDIR():
    if 'QTDIR' in os.environ:
        os.environ['PATH'] = os.path.join(os.environ['QTDIR'], 'bin') \
                + os.pathsep + os.environ['PATH']

