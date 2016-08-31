wikipedia-ngram
===============
Get all ngrams from (english) wikipedia-dump.

First
-----
You need to download the wikipedia dump
(e.g. see https://dumps.wikimedia.org/enwiki/).

```
cd dataset
./download.sh
```
should download the latest wikipedia dump of all article texts.

Process Data
------------
After you successfully downloaded the dataset, you can run:
```
buildngrams.py
```