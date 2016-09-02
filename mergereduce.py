#!/usr/bin/env python3
import sys
import os
import argparse
from multiprocessing import Pool
import multiprocessing
import fileinput



def main(params):
    parser = argparse.ArgumentParser(description='wikipedia ngram reduced merger', epilog="stg7 2016")

    infiles = list(filter(lambda x: "ngram." in x and ".red" in x, os.listdir(".")))
    print(infiles)
    os.system("sort -m {files} | gzip > merged_ngrams.gz".format(files=" ".join(infiles)))
    os.system("zcat merged_ngrams.gz | ./reducengram.py | lzma -9 -c -T 0 --stdout > reduced_ngrams.lzma")


if __name__ == "__main__":
    main(sys.argv[1:])
