# Disk & Memory Monitoring — keep storage and RAM healthy

Check storage

- `df -h` — shows mounted filesystems and free space (human-readable)
- `du -sh /path/to/folder` — disk usage of a folder
- `lsblk` — list block devices and partitions

Check memory and load

- `free -m` — memory and swap usage in MB
- `vmstat 1 5` — quick snapshot of system activity
- `uptime` — system load averages (1/5/15 min)

Cleaning tips

- Find large files: `find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null`
- Empty package caches (example for apt): `sudo apt clean`

Example: check `/var/log` usage

```bash
du -sh /var/log
df -h /
```

Exercise (5–10 minutes)

1. Run `df -h` and identify the filesystem with the least free space.
2. Run `free -m` and note total and used memory.

Hints:
```bash
df -h
free -m
```

Where to go next

- Continue to `linux-commands/07-networking.md` to check network health and connectivity.
