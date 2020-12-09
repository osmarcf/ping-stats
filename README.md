# ping-stats

Python script to send ICMP requests to hosts using the network interfaces defined.
It uses Python 2.7.9 because it runs on an Orange Pi and I didn't want to upgrade the Python version.

This script loops two arrays: hosts and network interfaces. Then it open a OS process to send a ping command.
The response from this command forms a few data (response time duration and its time measurement unit).
The host, interface duration and time unit are "converted" to a JSON or CSV format and written to a file.

To reduce disk usage, I've added a cron job to gzip the file every day:
```
 0 0 * * * gzip -S "_`date +%Y-%m-%d`.gz" /tmp/dados_ping.csv
```

Remember: /tmp generally is mounted on a tmpfs, so it is volatile. On poweroff, it's all lost.
