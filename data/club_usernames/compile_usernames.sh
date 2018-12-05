#!/bin/bash

# Loop through all folders in current directory
# Outputs a csv representing unique usernames

directories=(*/)

for dir in "${directories[@]}"; do
	cat $dir/* | sort -u > $dir_unique_users.csv
done
#for f in *; do
#	if [[ -d $f ]];
#	then
#		echo Processing $f ...
#		cat $f/* | sort -u > $f_unique_users.csv
#	fi
#done




#cat 1-10000/* | sort -u > c10000-20000.csv
