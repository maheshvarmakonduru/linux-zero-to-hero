# Scenario: Server Down — step-by-step troubleshooting

Problem: users report the website is unreachable and pings fail or the service returns errors.

Step 0 — confirm reachability

- From your laptop: `ping -c 4 example.com` or `curl -I http://example.com`.

Step 1 — connect to the server

- `ssh admin@web-01` (use your host or IP). If SSH fails, check network/firewall from a nearby host.

Step 2 — quick health checks

- `uptime` — check load averages
- `top` or `htop` — see CPU/memory usage
- `df -h` — check disk space (a full disk often causes failures)

Step 3 — check service status and logs

- `sudo systemctl status nginx` (replace `nginx` with your service)
- `sudo journalctl -u nginx --since "30 minutes ago" | tail -n 200`
- If service shows `failed` or `exited`, the logs usually show why.

Step 4 — common fixes

- Full disk: identify large files `du -sh /var/log/* | sort -h` and rotate/cleanup logs.
- Permission issues: check ownership of log or web folders and fix with `chown`.
- Port conflicts: `ss -tulnp | grep :80` to see what is listening.

Step 5 — restart carefully

- `sudo systemctl restart nginx` then `sudo systemctl status nginx`.
- If restart fails, do not repeatedly restart — collect logs and increase verbosity if possible.

Step 6 — rollback or restore

- If a recent deploy caused the problem, roll back to previous release and restart the service.

Documentation to attach to an incident report

1. `uname -a` and `cat /etc/os-release`
2. `df -h` output
3. `journalctl -u nginx -n 200 > nginx-logs.txt`
4. Steps you ran and timestamps
