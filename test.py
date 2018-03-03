#!/usr/bin/python

from __future__ import print_function

import sys
import glob
import trparse

def main():
    
    if len(sys.argv) == 1:
        print("Missing test files")
        sys.exit(1)

    for file_pattern in sys.argv[1:]:

        filenames = glob.glob(file_pattern)

        for filename in filenames:
            with open(filename, 'r') as f:
                
                print("Loading {}".format(filename))
                tr = trparse.load(f)

                print("Dumping")
                print(tr)

if __name__ == "__main__":
    main()
