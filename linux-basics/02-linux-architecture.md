# Linux Architecture — simple map for beginners

Linux can be thought of as layered software. Each layer has a job — understanding them helps you diagnose problems faster.

Layers you should know:

- Hardware: CPU, memory (RAM), disks, and network interfaces — the physical parts.
- Kernel: the central piece of Linux that talks to hardware, manages processes, memory, drivers, and networking.
- System services (init/systemd): start and manage background services like web servers and schedulers.
- Shell & user space: the shell (bash, zsh) is your command-line interface; user space contains applications you run (editors, web servers).

Quick commands to explore the architecture

- `uname -r` — kernel version
- `top` or `htop` — running processes and resource usage
- `ps aux | head` — snapshot of active processes
- `systemctl status sshd` — show status of a service (replace `sshd` with any service)

Real-world troubleshooting example

Problem: a web app is slow.
Steps a beginner can try:
1. Check CPU/memory: `top` (look for processes using lots of CPU/RAM).
2. Check disk usage: `df -h` (a full disk can make apps fail).
3. Check the web server service: `systemctl status nginx` or `journalctl -u nginx --since "1 hour ago"`.

Beginner exercise (5–10 minutes)

1. Run `uname -r` and `top` for 30 seconds to observe processes.
2. Run `ps aux | grep -E "ssh|nginx|apache|docker"` to see if common services are running.

Where to go next

- Read `linux-basics/04-linux-filesystem.md` to understand where logs and configs live.
- Continue to `linux-commands/05-process-management.md` to learn how to manage processes safely.
