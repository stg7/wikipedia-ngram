#!/usr/bin/env python3
import sys
import os
import argparse

def main(params):
    parser = argparse.ArgumentParser(description='wikipedia ngram extractor', epilog="stg7 2016")
    parser.add_argument('infile', type=str, help="wikipedia input file")
    parser.add_argument('-o', type=str, help="ngram output directory")

    argsdict = vars(parser.parse_args())


if __name__ == "__main__":
    main(sys.argv[1:])
