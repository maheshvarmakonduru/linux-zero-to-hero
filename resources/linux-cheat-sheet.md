# Linux Quick Cheat Sheet — core commands (one page)

Navigation
- `pwd` — print working directory
- `cd /path` — change directory
- `ls -lah` — list files (hidden + human sizes)

Files
- `cat file` — show file
- `head -n 10 file` / `tail -n 10 file` — preview
- `less file` — scroll

Create/Modify
- `touch file` — create
- `mkdir -p folder` — create folders
- `cp src dest` / `mv src dest` — copy/move
- `rm file` / `rm -rf folder` — remove (dangerous)

Search & Filter
- `grep -n "pattern" file` — search with line numbers
- `find /path -type f -name "*.log"` — find files

Processes & Services
- `top` / `htop` — live processes
- `ps aux | grep name` — find processes
- `sudo systemctl status svc` — service status
- `journalctl -u svc -n 200` — service logs

Disk & Memory
- `df -h` — filesystem usage
- `du -sh folder` — folder size
- `free -h` — memory

Networking
- `ip a` — interfaces
- `ping 8.8.8.8` — reachability
- `curl -I https://example.com` — HTTP headers

Permissions
- `ls -l` — owner & perms
- `chmod +x file` — make executable
- `chown user:group file` — change owner

Archiving
- `tar -czvf a.tar.gz folder` — create archive
- `tar -xzvf a.tar.gz` — extract

Notes
- Use `--help` and `man` for command details.
- Prefer interactive `rm -ri` when learning.
