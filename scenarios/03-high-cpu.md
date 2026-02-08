# Scenario: High CPU Usage — investigate without panic

Problem: system load is high and users notice slowness.

Step 1 — observe

- `uptime` — check load averages
- `top` or `htop` — sort by `%CPU` to find the top consumers
- `ps aux --sort=-%cpu | head -n 20` — snapshot of heavy processes

Step 2 — inspect the process

- `strace -p <PID> -c` — sample system calls to see what the process is doing (requires root)
- `lsof -p <PID>` — open files and sockets used by the process

Step 3 — take safe actions

- If a runaway process is non-critical, stop it gracefully: `kill <PID>` then `kill -9 <PID>` if it does not stop.
- Use `nice` or `renice` to lower priority: `sudo renice +10 -p <PID>`.

Step 4 — find root cause and prevent

- Check recent deploys, cron jobs, or backups that could cause spikes.
- Add monitoring/alerts for high CPU and record a playbook for future incidents.

Example quick commands

```bash
ps aux --sort=-%cpu | head -n 10
sudo renice +10 -p 12345
sudo systemctl restart my-service
```

