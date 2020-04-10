#!/bin/bash
while true
do
	a=$[`date -d "$timestart" +%s`/3600]
	tcpdump  -G 3600 -i eth0  -s 0 -w /usr/local/src/tcpdump_filter/log/$a > /dev/null 2>&1
done
