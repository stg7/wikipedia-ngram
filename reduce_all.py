#!/usr/bin/env python3
import os
import sys
import argparse
from multiprocessing import Pool
import multiprocessing


def do_it(cmd):
    r = os.system(cmd)
    if r != 0:
         sys.exit(1)
         print(cmd + " done")

def main(params):
    parser = argparse.ArgumentParser(description='wikipedia ngram reducer', epilog="stg7 2016")
    parser.add_argument('--cpu_count',type=int, default=multiprocessing.cpu_count(), help='thread/cpu count')

    argsdict = vars(parser.parse_args())
    cpu_count = argsdict["cpu_count"]

    commands = []
    for f in os.listdir("."):
        if "ngram" in f[0:len("ngram")]:
            command = "cat {ngram} | sort | ./reducengram.py > {ngram}.red ".format(ngram=f)
            commands.append(command)

    print(commands)

    pool = Pool(processes=cpu_count)
    pool.map(do_it, commands)


if __name__ == "__main__":
    main(sys.argv[1:])