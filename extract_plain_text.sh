#!/bin/bash

python3 ./tools/wikiextractor/WikiExtractor.py -c -o out dataset/*wiki-*-pages-articles-multistream.xml.bz2
