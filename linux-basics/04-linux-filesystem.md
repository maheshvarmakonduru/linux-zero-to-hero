# Linux File System Overview — where things live

Linux organizes files into a single hierarchy starting at `/` (root). Knowing common folders helps you find logs, configs, and user files quickly.

Key directories and what they contain:

- `/` — root of the filesystem. Everything starts here.
- `/bin` — essential user commands (ls, cp, mv).
- `/sbin` — system binaries (fsck, ifconfig) usually for admins.
- `/usr` — user programs and libraries (shared apps).
- `/etc` — configuration files for the system and services.
- `/var` — variable data like logs (`/var/log`), caches, and mail.
- `/home` — personal folders for users (e.g., `/home/mahesh`).
- `/tmp` — temporary files (often cleared on reboot).
- `/proc` and `/sys` — virtual filesystems exposing kernel and process info (`/proc/cpuinfo`).
- `/boot` — boot loader files and kernels.

Absolute vs relative paths

- Absolute: starts with `/` (example: `/etc/hosts`).
- Relative: based on your current folder (example: `./notes.txt` or `../` to go up one level).

Permissions quick note

- Use `ls -l` to see permissions and owners: `-rw-r--r-- 1 user group size file`
- `chmod` changes permissions; `chown` changes owner. We cover these in `linux-commands/03-permissions-ownership.md`.

Example: checking web server logs

```bash
ls -lh /var/log/nginx/
tail -n 50 /var/log/nginx/error.log
```

Beginner exercise (5 minutes)

1. Run `ls -la /` and `ls -la /home` to see folders and owners.
2. Run `cat /etc/os-release` to confirm OS details.

Where to go next

- Continue to `linux-commands/01-file-directory-commands.md` to practice navigation and file commands.
