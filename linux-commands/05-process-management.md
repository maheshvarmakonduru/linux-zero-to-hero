# Process Management — keep systems responsive

Often you'll need to see what's running, stop runaway programs, or run tasks in the background.

Viewing processes

- `top` — interactive view of CPU/RAM usage (press `q` to quit)
- `htop` — nicer interactive viewer (if available)
- `ps aux | less` — static snapshot of all processes

Find and stop processes

- `ps aux | grep name` — find processes by name
- `kill <PID>` — send TERM signal to gracefully stop a process
- `kill -9 <PID>` — force kill (use only when necessary)
- `pkill -f process_name` — kill by name or match

Job control

- `&` — run a command in the background: `sleep 60 &`
- `jobs` — list background jobs
- `fg %1` — bring job 1 to foreground
- `bg %1` — continue job 1 in background

Nice and priorities

- `nice -n 10 command` — run a command with lower priority
- `renice -n 5 -p <PID>` — change priority of running process

Service management (systemd)

- `systemctl status nginx` — check service status
- `sudo systemctl start|stop|restart nginx` — manage services
- `journalctl -u nginx --since "1 hour ago"` — view service logs

Exercise (5–10 minutes)

1. Run `top` for 10 seconds and note the highest CPU process.
2. Start a background sleep: `sleep 120 &`, then list it with `jobs` and bring it to foreground.

Hints:
```bash
sleep 120 &
jobs
fg %1
```

Where to go next

- Next: `linux-commands/06-disk-memory.md` to check storage and memory health.
