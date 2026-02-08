# Advanced Practice — automation, backup, and debugging

Exercise 1 — Scheduled backups with cron (15–20 minutes)

1. Write a small backup script `~/bin/backup-home.sh` that tars your home `~/notes` folder and stores it in `~/backups/` with a timestamp.
2. Add a cron job that runs daily at 02:00.

Example script:
```bash
#!/bin/bash
mkdir -p ~/backups
tar -czf ~/backups/notes-$(date +"%F-%H%M").tar.gz -C ~ notes
```

Add to crontab with `crontab -e`:
```cron
0 2 * * * /home/$USER/bin/backup-home.sh
```

Exercise 2 — Automated health check (15 minutes)

1. Create a script `check-health.sh` that checks `df -h`, `free -m`, and `systemctl is-active nginx` and returns non-zero if a check fails.
2. Run it and examine outputs.

Exercise 3 — Container/Service cleanup (15 minutes)

1. For systems with Docker: list images and remove dangling images.

Commands:
```bash
docker images -f "dangling=true"
docker image prune -f
```

Exercise 4 — Troubleshoot and document a failing service (20 minutes)

1. Pick a service (nginx, apache, or a sample app). Collect logs with `journalctl -u <service> -n 200`.
2. Attempt a safe restart and document the before/after state.

Where to go next

- Use `scenarios/` to practice real-world step-by-step troubleshooting examples.
