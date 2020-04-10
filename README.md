# Overview
tcpdump_filter is a syn-flood monitor tool base on tcpdump. It can auto filter attacker ip address.

# Usage
start do_tcpdump.sh it can generate log per hour.
```
./do_tcpdump.sh &
```
start cron and filter log.
```
crontab -e
* */1 * * * /usr/local/src/tcpdump_filter/transition.sh > /dev/null 2>&1 &
systemctl reload crond
```
