#!/bin/sh

#This shell script is used to concatenate all csv files resulting from scrapes

root_dir=`(cd ..; pwd)`
echo "root directory: $root_dir"

#remove previous list
rm -f $root_dir/data/processed/animelists.csv

#Combine all files in Forum_usernames
cd $root_dir/data/user_anime_list
find . -name '*.csv' | xargs -n 1000 -P 8 cat >> $root_dir/data/processed/animelists.csv

#remove tmp folder and print how many usernames
wc -l $root_dir/data/processed/animelists.csv 

