#!/usr/bin/env python
# cbtest
# Copyright (C) ContinuumBridge Limited, 2017 - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Peter Claydon
#
import sys
from twisted.internet import reactor

def delayPrint()
    print("Delayed print")
    reactor.stop()
    exit()

def main():
    print("Hello world. This is a cbtest. Now for a 5 second delay")
    reactor.callLater(5, delayPrint)
    reactor.run()

if __name__ == '__main__':
    main()
