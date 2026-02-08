# Scenario: Disk Full — safe recovery steps

Problem: a server reports "No space left on device" or services fail to start.

Step 1 — confirm and locate

- `df -h` — find which filesystem is full.
- `du -sh /* 2>/dev/null | sort -h` — find large top-level folders.
- `du -sh /var/* 2>/dev/null | sort -h` — check `/var` where logs often grow.

Step 2 — identify largest files

- `find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | sort -k5 -h` — find files bigger than 100MB.

Step 3 — safe cleanup options

- Rotate and compress logs: `sudo logrotate` configuration or compress old logs with `gzip`.
- Clear package caches (Ubuntu): `sudo apt clean`
- Remove old kernels (use distro-specific tips) or prune Docker images: `docker image prune -a` (careful on production).

Step 4 — temporary relief

- Move large archives to another disk or `scp` them off the server.
- If removing, use interactive removal: `rm -ri /path/to/large`.

Example sequence

```bash
df -h
du -sh /var/* | sort -h
find /var/log -type f -name "*.log" -mtime +30 -exec gzip {} \;
sudo apt clean
```

Prevention

- Configure `logrotate` with compression and retention
- Monitor disk with alerts (use `du` and `df` checks in health scripts)

