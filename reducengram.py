#!/usr/bin/env python3
import sys
import os
import argparse
from multiprocessing import Pool
import multiprocessing
import fileinput


def main(params):
    parser = argparse.ArgumentParser(description='wikipedia ngram extractor', epilog="stg7 2016")
    current_ngram = ""
    first = True
    sumfreq = 0
    for line in fileinput.input():
        ngram, freq = line.strip().split("\t", 1)
        freq = int(freq)
        sumfreq += freq
        if first:
            current_ngram = ngram
            first = False

        if current_ngram != ngram:
            print("\t".join([ngram, str(sumfreq)]))
            sumfreq = 0
            current_ngram = ngram


if __name__ == "__main__":
    main(sys.argv[1:])
