#!/bin/sh

GoogleScraper --keyword-file keywords -s google -p 3 -m http -o main.json 

# cat main.json

python main.py

