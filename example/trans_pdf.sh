#!/bin/bash

( cd ../ && [[ ! -d tmp ]] && mkdir tmp
pdftotext example/vldb14-pubsub.pdf tmp/dest_en_words.txt
cat tmp/dest_en_words.txt | awk '{for (i=1; i<NF;i++) print $i}'  | sort | uniq -c | sort -nr > tmp/en_uniq_words_list.txt
python3 trans_words.py tmp/en_uniq_words_list.txt > example/vldb14-pubsub_words_zh.txt
rm -rf tmp/dest_en_words.txt tmp/en_uniq_words_list.txt
)

