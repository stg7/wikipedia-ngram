#!/bin/bash
release="20160801"
wget "https://dumps.wikimedia.org/enwiki/"

release="$(cat index.html | grep -B 1 "latest" | head -n 1 | sed "s|.*\">||g" | sed "s|/.*||g")"
rm index.html

wget -c "https://dumps.wikimedia.org/enwiki/$release/enwiki-$release-pages-articles-multistream.xml.bz2"
wget -c "https://dumps.wikimedia.org/enwiki/$release/enwiki-$release-pages-articles-multistream-index.txt.bz2"

