#!/usr/bin/env python3
import sys
import os
import argparse
from multiprocessing import Pool
import multiprocessing
import fileinput


def find_ngrams(input_list, n):
    """ from http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/ """
    return list(zip(*[input_list[i:] for i in range(n)]))


def get_ngrams(text):
    words = text.split()
    ngrams = []
    for n in range(1, 6):
        ngrams += [" ".join(x) for x in find_ngrams(words, n)]
    return ngrams


def extract_ngram(params):
    infile, outfile = params
    print(infile)
    docs = []
    cdoc = ""
    for line in fileinput.FileInput(infile, openhook=fileinput.hook_compressed):
        l = str(line)
        if "</doc>" in l:
            docs.append(cdoc.replace("\n", " "))
            cdoc = ""
        else:
            if "<doc" not in l:
                cdoc += l
    # TODO: write a compressed file
    f = open(outfile, "a")
    for d in docs:
        ngrams = get_ngrams(d)
        for x in ngrams:
            f.write(x + "\t1\n")
    f.close()


def main(params):
    parser = argparse.ArgumentParser(description='wikipedia ngram extractor', epilog="stg7 2016")
    parser.add_argument('infile', nargs="+", type=str, help="wikipedia input files")
    parser.add_argument('-o', type=str, help="ngram output directory")
    parser.add_argument('--cpu_count', type=int, default=multiprocessing.cpu_count(), help='thread/cpu count')
    parser.add_argument('-c', dest='clean', action='store_true', help='clean older results')

    argsdict = vars(parser.parse_args())
    cpu_count = argsdict["cpu_count"]

    if argsdict['clean']:
        os.system("rm -rf ngram.*")

    infiles = argsdict["infile"]
    print(infiles)
    pool = Pool(processes=cpu_count)
    outfiles = ["ngram." + str(i % cpu_count) for i in range(0, len(infiles))]
    params = zip(infiles, outfiles)
    pool.map(extract_ngram, params)

    # sort each outputfile
    for of in outfiles[0:cpu_count]:
        print(of)

    # merge calculated values in each outfile

    # reduce each output file

if __name__ == "__main__":
    main(sys.argv[1:])
