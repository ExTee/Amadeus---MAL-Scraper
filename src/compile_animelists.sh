#!/bin/sh

#This shell script is used to concatenate all csv files resulting from scrapes
#Stores resulting file in data/processed/animelists.csv

root_dir=`(cd ..; pwd)`
echo "Compiling user anime lists ..."
echo "root directory: $root_dir"

#move previous list
mv $root_dir/data/processed/animelists.csv $root_dir/data/.old/old_animelists.csv

#Create temporary folder, output new result in temp folder
cd $root_dir/data/user_anime_list
mkdir $root_dir/data/tmp
find . -name '*.csv' | xargs -n 1000 -P 8 cat >> $root_dir/data/tmp/animelists.csv

#Check for differences with old and save
cat $root_dir/data/tmp/animelists.csv $root_dir/data/.old/old_animelists.csv | sort -u > $root_dir/data/processed/animelists.csv

#remove tmp folder and print how many usernames
rm -rf $root_dir/data/tmp
wc -l $root_dir/data/processed/animelists.csv 

