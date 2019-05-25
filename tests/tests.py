#!/usr/bin/python
import sys
import glob
import trparse

from unittest import TestCase

FILE_PATTERN = './data/*.txt'


class TracerouteTestCase(TestCase):

    def setUp(self):
        self.filenames = glob.glob(FILE_PATTERN)

    def test_simple(self):
        for filename in self.filenames:
            with open(filename, 'r') as f:
                tr = trparse.load(f)
                str(tr)
