#!/usr/bin/env python

"""
Runs all tests in the 'authorize' package.
"""

from optparse import OptionParser
from os.path import dirname, join
import sys
import unittest

CURRENT_DIR = dirname(__file__)

def runtests(*test_args, **opts):
    suite = unittest.defaultTestLoader.discover(
        start_dir=join(CURRENT_DIR, "authorize", "tests"),
        top_level_dir=CURRENT_DIR,
    )
    result = unittest.TextTestRunner(**opts).run(suite)
    sys.exit(not result.wasSuccessful())

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', action='store', default=1, dest='verbosity', type="int")
    parser.add_option('--failfast', action='store_true', default=False, dest='failfast')

    (options, args) = parser.parse_args()
    runtests(failfast=options.failfast, verbosity=options.verbosity, *args)





