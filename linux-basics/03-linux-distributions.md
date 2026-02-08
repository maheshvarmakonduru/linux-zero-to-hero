# Linux Distributions — picking the right one

A Linux distribution (distro) bundles the Linux kernel with system tools, libraries, and a package manager so you can install software easily.

Popular distros and where they shine:

- Ubuntu: beginner-friendly, large community, great for desktops and cloud VMs.
- Debian: very stable; often used where conservatism and stability matter.
- CentOS / Rocky Linux / AlmaLinux: common in enterprise servers (RHEL-compatible).
- Fedora: cutting-edge packages, often used by people who want newer software.
- Arch: rolling-release and very configurable (advanced users).
- Amazon Linux: tuned for AWS environments.

Package managers (how you install software):

- Debian/Ubuntu: `apt` (example: `sudo apt update && sudo apt install curl`)
- RHEL/CentOS/Rocky: `dnf` or `yum` (example: `sudo dnf install httpd`)
- Arch: `pacman`

Choosing a distro — quick guide:

- If you're new: start with Ubuntu (server or desktop) — lots of tutorials match it.
- For enterprise job-readiness: learn a RHEL/CentOS-like system and Ubuntu.
- For cloud: Ubuntu and Amazon Linux are very common.

Beginner exercise (5 minutes)

1. On any Linux machine run `cat /etc/os-release` to see which distro you're on.
2. Try installing a small utility (example uses Ubuntu):

```bash
sudo apt update
sudo apt install -y cowsay
cowsay "Hello from my distro"
```

If `apt` is not available, your system uses a different package manager — try `dnf`, `yum`, or `pacman`.

Where to go next

- Continue with `linux-basics/04-linux-filesystem.md` to learn where system files live on any distro.
