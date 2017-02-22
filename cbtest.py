#!/usr/bin/env python
# cbtest
# Copyright (C) ContinuumBridge Limited, 2017 - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Peter Claydon
#
import sys
import os
from  testdir.test1 import test1

def main():
    print("Hello world. This is a cbtest.")
    CB_BID = os.getenv('CB_BID', 'unconfigured')
    print("CB_BID: {}".format(CB_BID))
    test1()

if __name__ == '__main__':
    main()
