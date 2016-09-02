#!/bin/bash
./prepare.sh

cd dataset
./download.sh
cd ..

./extract_plain_text.sh
./buildngrams.py out/*/*.bz2

./reduce_all.py
./mergereduced.py
