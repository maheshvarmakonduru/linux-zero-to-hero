# Linux Zero to Hero – Full Commands Cheat Sheet

This is a complete reference of Linux commands that are most useful for **DevOps engineers, software developers, and cloud professionals**.

---

## 🔹 File & Directory Operations
- `pwd` → Print working directory
- `cd /path` → Change directory
- `ls` → List files
- `ls -la` → List all files including hidden
- `mkdir folder` → Create directory
- `rmdir folder` → Remove empty folder
- `rm -rf folder` → Remove folder recursively
- `touch file` → Create empty file
- `cp source dest` → Copy files
- `mv source dest` → Move or rename
- `tree` → Show directory tree

---

## 🔹 File Viewing & Editing
- `cat file` → View file content
- `less file` → Scrollable file view
- `more file` → View file page by page
- `head file` → First 10 lines
- `tail file` → Last 10 lines
- `tail -f file` → Monitor logs live
- `nano file` → Simple editor
- `vim file` → Advanced editor

---

## 🔹 Permissions & Ownership
- `ls -l` → Detailed view
- `chmod 644 file` → Change permissions
- `chown user:group file` → Change ownership
- `chgrp group file` → Change group

---

## 🔹 Searching & Filtering
- `grep "text" file` → Search text
- `grep -r "text" /path` → Recursive search
- `find /path -name "*.log"` → Find files by name
- `locate file` → Find file quickly
- `awk '{print $1}' file` → Extract column
- `sed 's/old/new/g' file` → Replace text

---

## 🔹 Process Management
- `ps aux` → List processes
- `top` → Interactive CPU/memory monitor
- `htop` → Enhanced top (if installed)
- `kill PID` → Kill process
- `pkill name` → Kill by process name
- `jobs` → List background jobs
- `bg` → Resume job in background
- `fg` → Bring job to foreground

---

## 🔹 Disk & Memory
- `df -h` → Disk usage
- `du -sh folder` → Folder size
- `free -m` → Memory usage
- `uptime` → System load
- `vmstat` → Memory & CPU stats
- `iostat` → Disk IO stats (install sysstat)

---

## 🔹 Networking
- `ip a` → View IP addresses
- `ping 8.8.8.8` → Test connectivity
- `ss -tulnp` → Listening ports
- `netstat -tulnp` → Legacy port info
- `curl https://example.com` → Fetch URL
- `wget url` → Download file
- `scp file user@remote:/path` → Copy remotely
- `rsync -av source dest` → Sync files

---

## 🔹 Package Management (Ubuntu)
- `sudo apt update` → Refresh repository
- `sudo apt upgrade` → Upgrade packages
- `sudo apt install package` → Install
- `sudo apt remove package` → Remove
- `dpkg -l` → List installed packages
- `snap list` → List snap packages

---

## 🔹 Compression & Archiving
- `tar -czvf archive.tar.gz folder` → Compress
- `tar -xzvf archive.tar.gz` → Extract
- `zip file.zip folder` → Zip folder
- `unzip file.zip` → Extract zip
- `gzip file` → Compress file
- `gunzip file.gz` → Decompress

---

## 🔹 System Info
- `uname -a` → Kernel info
- `hostname` → Hostname
- `whoami` → Current user
- `id` → User ID
- `uptime` → Load & uptime

---

## 🔹 DevOps Commands
- `systemctl start|stop|status service` → Manage services
- `journalctl -xe` → Check logs
- `crontab -e` → Schedule jobs
- `docker ps` → List containers
- `docker logs container` → Container logs
- `kubectl get pods` → Kubernetes pods
- `kubectl logs pod` → Pod logs

---

## 🔹 Miscellaneous
- `date` → Show date & time
- `cal` → Show calendar
- `echo "text"` → Print text
- `history` → Command history
- `alias ll='ls -la'` → Create shortcut
- `uptime` → Load & uptime

> ⚡ Pro Tip: Combine commands using `|`, `&&`, `>` for real-world scenarios
