#!/bin/bash
a=$[`date -d "$timestart" +%s`/3600]
echo $a
dir=./log
for file in $dir/*; do
	purefile=${file:6:6}
	b=$(echo $file | grep txt)
	if [[ $purefile = $a ]] || [[ $b != "" ]]; then
		echo $file
	else
		tcpdump -r $file>$file.txt
		rm -rf $file
	fi
	python filter_black_list.py   
done

