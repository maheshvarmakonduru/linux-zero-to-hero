# What is Linux?

Linux is the core software layer (the kernel) that helps programs talk to your computer's hardware. Think of it as the manager in an office who assigns tasks, keeps things organized, and makes sure everyone follows the rules.

Key points for beginners:

- Linux is open-source: anyone can read, modify, and share it.
- It’s used on servers, cloud virtual machines, laptops, phones (Android), and many devices.
- It’s multi-user and multi-tasking: many people and programs can use the machine at once.
- It's stable and efficient, which is why servers use it a lot.

Why learn Linux first?

- Most servers and cloud systems run Linux.
- Many developer tools and deployment systems expect Linux knowledge.
- Learning Linux helps you understand how software runs in real environments.

Basic commands to see Linux on your machine

Open a terminal and try these commands. Each one is followed by a short explanation and an example of what you might see.

```bash
# show kernel name, version, and basic system info
uname -a

# show distribution details (Ubuntu, Fedora, etc.)
cat /etc/os-release

# show systemd managed info on many systems (friendly output)
hostnamectl

# who am I? (your login name)
whoami

# how long the system has been running and load
uptime
```

Example outputs (yours may differ):

```text
uname -a
Linux my-laptop 5.15.0-60-generic #66-Ubuntu SMP Thu Jun 2 15:07:40 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

cat /etc/os-release
NAME="Ubuntu"
VERSION="22.04 LTS (Jammy Jellyfish)"
ID=ubuntu

hostnamectl
	Static hostname: my-laptop
			Icon name: laptop
		  Machine ID: xxxxx
			  Chassis: laptop
		  Operating System: Ubuntu 22.04 LTS
					  Kernel: 5.15.0-60-generic
			 Architecture: x86-64

whoami
mahesh

uptime
 10:34:21 up 2:15, 2 users, load average: 0.12, 0.08, 0.05
```

Short plain-language translations:

- `uname -a`: tells you which Linux kernel version you're running.
- `cat /etc/os-release`: shows the distribution name (Ubuntu, CentOS, etc.) and version.
- `hostnamectl`: provides a neat summary including machine name and OS name.
- `whoami`: your current username on the system.
- `uptime`: how long the system has been up, and how busy it is.

Real-world story: imagine you are the person who needs to deploy a web app to a cloud server. The first things you'll confirm are "what OS is on this server?" and "is it healthy?" — the commands above answer those questions quickly.

Beginner exercise (5 minutes)

1. Open a terminal on your machine (Terminal on macOS, WSL/PowerShell on Windows, or a Linux VM).
2. Run `uname -a` and `cat /etc/os-release`.
3. Copy the outputs into a new file named `my-first-linux-info.txt` in this repo and commit it (or just save it in a folder).

Hint: create the file with:

```bash
uname -a > my-first-linux-info.txt
cat /etc/os-release >> my-first-linux-info.txt
```

Solution example (what `my-first-linux-info.txt` might contain):

```text
Linux my-laptop 5.15.0-60-generic #66-Ubuntu SMP ... x86_64 GNU/Linux
NAME="Ubuntu"
VERSION="22.04 LTS (Jammy Jellyfish)"
```

Where to go next

- Read `linux-basics/02-linux-architecture.md` to understand components like kernel, shell, and user space.
- Then open `linux-commands/01-file-directory-commands.md` to start practicing navigation and file commands.
