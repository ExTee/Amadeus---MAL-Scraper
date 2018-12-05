#!/bin/sh

#	This shell script is used to concatenate all csv files resulting from scrapes

root_dir=`(cd ..; pwd)`
echo "root directory: $root_dir"

#Clears and Creates tmp folder
rm -rf $root_dir/data/tmp
mkdir $root_dir/data/tmp

#Combine all files in Forum_usernames
cd $root_dir/data/forum_usernames
find . -name '*.csv' | xargs -n 1000 -P 8 cat >> $root_dir/data/tmp/compiled_forum_usernames

#Combine all files in Club_usernames
cd $root_dir/data/club_usernames
find . -name '*.csv' | xargs -n 1000 -P 8 cat >> $root_dir/data/tmp/compiled_club_usernames

#Combine everything and outputs one file
cd $root_dir/data/tmp
cat compiled_forum_usernames compiled_club_usernames | sort -u > $root_dir/data/usernames.csv

#remove tmp folder and print how many usernames
rm -rf $root_dir/data/tmp
wc -l $root_dir/data/usernames.csv 


