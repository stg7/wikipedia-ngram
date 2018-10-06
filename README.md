# wikipedia-ngram
Get all ngrams from (english) wikipedia-dump.

## Steps
First you need to download all required tools using
```
./prepare.sh
```

Then you can download latest wikipedia dump
(e.g. see https://dumps.wikimedia.org/enwiki/) with:
```
cd dataset
./download.sh
cd ..
```

As next step, you need to extract all plaintexts from wiki-dump:
```
./extract_plain_text.sh
```

Now you can build ngrams with the following commands:
```
# extract simply all ngrams to seperate files
./buildngrams.py out/*/*.bz2

# combine ngrams
./reduce_all.py

# merge and reduce
./mergereduced.py
```
