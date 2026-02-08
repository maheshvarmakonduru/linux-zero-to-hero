# Scenario: Permission Denied — diagnose and fix ownership/permissions safely

Symptoms: error messages like "Permission denied" when accessing files, writing logs, or starting services.

Step 1 — inspect

- `ls -l /path/to/file` — view owner and permissions
- `stat /path/to/file` — detailed file metadata

Step 2 — common causes

- Wrong owner/group (app runs as `www-data` but files owned by `root`)
- Missing write permission for the user or group
- SELinux/AppArmor restrictions (on some distros)

Step 3 — fix safely

- Change owner: `sudo chown -R www-data:www-data /var/www/myapp`
- Adjust permissions: `sudo chmod 640 /path/to/file` (example; avoid 777)

Step 4 — SELinux/AppArmor notes

- If `ls -Z` shows SELinux labels, use `restorecon` or `semanage` to fix contexts.
- AppArmor may block program access; check `dmesg` or `journalctl` for denials.

Example

```bash
ls -l /var/www/myapp
sudo chown -R www-data:www-data /var/www/myapp
sudo chmod -R 750 /var/www/myapp
```

Where to go next

- After fixing permissions, re-attempt the failing operation and check logs with `journalctl -xe`.

