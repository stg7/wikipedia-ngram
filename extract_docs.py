#!/usr/bin/env python3
import sys
import os
import argparse
from multiprocessing import Pool
import multiprocessing
import glob
import fileinput

def find(dirname):
    tmp = glob.glob(dirname + "/*")
    r = []
    for p in tmp:
        if os.path.isdir(p):
            r += find(p)
        else:
            r.append(p)
    return r

def extract_doc(infile, outdir):
    doc_start = False
    doc = ""
    doc_title = ""
    doc_id = ""

    try:
        fi = fileinput.FileInput(infile, openhook=fileinput.hook_compressed)

        for line in fi:
            line = line.decode('utf-8')
            if doc_start and not "</doc" in line:
                doc += line
            if "<doc" in line:
                doc_start = True
                doc_id = line.split("id=\"")[1].split("\"")[0]
                doc_title = line.split("title=\"")[1].split("\"")[0]
            if "</doc>" in line:
                doc_start = False
                print((doc_id, doc_title))
                if doc_id != "":
                    path = os.path.dirname(infile)
                    outpath = outdir + "/" + path + "/"
                    os.makedirs(outpath, exist_ok=True)
                    f = open(outpath + str(doc_id) + ".txt", "w")
                    f.write(doc)
                    f.close()
                doc = ""
                doc_id = ""
                doc_title = ""
        fi.close()
    except Exception as e:
        print("[error] " + str(e))

def main(params):
    parser = argparse.ArgumentParser(description='wiki doc extractor', epilog="stg7 2016", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--outdir', type=str, default="sep_txt", help='outdir of seperated txt files')
    parser.add_argument('indir', type=str, help='input directory')

    argsdict = vars(parser.parse_args())

    outdir = argsdict["outdir"]

    os.makedirs(outdir, exist_ok=True)
    if not os.path.isdir(argsdict["indir"]):
        print("[error] {} is not a dir".format(argsdict["indir"]))
        return 1

    infiles = find(argsdict["indir"])

    cpu_count = multiprocessing.cpu_count()
    pool = Pool(processes=cpu_count)
    pool.starmap(extract_doc, zip(infiles, [outdir for x in infiles]))



if __name__ == "__main__":
    main(sys.argv[1:])
