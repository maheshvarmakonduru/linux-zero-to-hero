# Package Management (Ubuntu)

- Package Management — install and update software

Different distros use different package managers. Here are common ones and how to use them.

Debian/Ubuntu (`apt`)

- `sudo apt update` — refresh package lists
- `sudo apt install -y package` — install a package
- `sudo apt remove package` — remove
- `apt list --installed` or `dpkg -l` — list installed packages

RHEL/CentOS (`dnf`/`yum`)

- `sudo dnf install package` or `sudo yum install package`

Arch (`pacman`)

- `sudo pacman -S package`

Example: install `curl` (Ubuntu)

```bash
sudo apt update
sudo apt install -y curl
curl --version
```

Exercise (5 minutes)

1. Update package lists on your machine (if you have a Linux VM) and search for `curl`.

Hints:
```bash
sudo apt update
apt search curl
```

Where to go next

- After installing tools, move to `linux-commands/07-networking.md` to use `curl`, `traceroute`, and other network tools.
