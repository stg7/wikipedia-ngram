#!/bin/bash

for ar in $(find out -name "*.bz2"); do
    path=$(echo "$ar" | sed "s|$(basename "$ar")||g" | sed "s|out|sep_txt|g")
    bzcat "$ar" | ./extract_docs.py "$path"

done