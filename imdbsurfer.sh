#!/bin/bash
echo "ScrapyCrawl begin"
date
inicio=$(date +"%s")
cd /home/eleonorvinicius/Projects/imdbsurfer
source bin/activate
scrapy crawl movies --logfile=scrapy_crawl.log --loglevel=ERROR
fim=$(date +"%s")
dif=$(($fim-$inicio))
horas=$(($dif/3600))
minutos=$((($dif%3600)/60))
segundos=$(($dif%60))
echo "ScrapyCrawl end: ${horas}:${minutos}:${segundos}"
date
