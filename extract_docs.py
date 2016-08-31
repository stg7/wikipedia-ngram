#!/usr/bin/env python3
import sys
import os
import argparse
from multiprocessing import Pool
import multiprocessing


def main(params):
    if len(params) == 0:
        outdir = "sep_txt/"
    else:
        outdir = params[0]

    os.makedirs(outdir, exist_ok=True)

    doc_start = False
    doc = ""
    doc_title = ""
    doc_id = ""

    for line in sys.stdin:
        if doc_start:
            doc += line
        if "<doc" in line:
            doc_start = True
            doc_id = line.split("id=\"")[1].split("\"")[0]
            doc_title = line.split("title=\"")[1].split("\"")[0]
        if "</doc>" in line:
            doc_start = False
            print((doc_id, doc_title))
            if doc_id != "":
                f = open(outdir + str(doc_id) + ".txt", "w")
                f.write(doc)
                f.close()
            doc = ""
            doc_id = ""
            doc_title = ""


if __name__ == "__main__":
    main(sys.argv[1:])
