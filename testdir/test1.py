#!/usr/bin/env python
# test1.py
# Copyright (C) ContinuumBridge Limited, 2017 - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Peter Claydon
#
import sys
import os
from twisted.internet import reactor

def delayPrint():
    print("Delayed print from test1")
    reactor.stop()

def test1():
    print("Hello, this is test1.py in the testdir directory")
    CB_BID = os.getenv('CB_BID', 'unconfigured')
    print("CB_BID: {}".format(CB_BID))
    reactor.callLater(5, delayPrint)
    reactor.run()

if __name__ == '__main__':
    test1()
