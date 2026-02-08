# Scenario: Application Not Starting — diagnose start failures

Problem: an application service fails to enter the `active` state or exits immediately after starting.

Step 1 — check the service

- `sudo systemctl status myapp` — shows recent logs and state
- `sudo journalctl -u myapp -n 200 --no-pager` — full recent logs

Step 2 — inspect environment and configuration

- Confirm config files in `/etc/myapp/` or wherever they live. Use `less`/`cat` to inspect.
- Check file ownership and permissions for config and data directories.
- If the app uses environment variables (systemd unit `EnvironmentFile`), ensure values are correct.

Step 3 — run manually for debugging

- Try starting the app manually under your user to see stdout/stderr: `sudo -u myappuser /usr/bin/myapp --config /etc/myapp/config.yml`
- Use `strace` or `gdb` for lower-level debugging if needed (advanced).

Step 4 — common quick fixes

- Missing dependencies: install required packages via package manager.
- Port already in use: `ss -tulnp | grep <port>` — find conflicting process.
- Database connection failures: verify credentials and network reachability.

Example sequence

```bash
sudo systemctl stop myapp
sudo journalctl -u myapp -n 200 > myapp.log
sudo -u myappuser /usr/bin/myapp --config /etc/myapp/config.yml
```

Where to go next

- After collecting logs and evidence, either restart the service carefully or roll back the last deploy.
