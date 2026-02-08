# Linux on macOS

macOS is Unix-based, so many Linux commands work natively. For a full Linux experience (reproducible labs and Docker work), follow the steps below.

**Optional steps:**
## 1) Install Homebrew (package manager)
Homebrew makes installing developer tools easy.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
```

After installation, follow any instructions printed by the installer to add Homebrew to your PATH.

## 2) Recommended apps and tools
- Install a better terminal (optional but useful):

```bash
brew install --cask iterm2
```

- Install a good editor:

```bash
brew install --cask visual-studio-code
```

## 3) Install Docker (for labs)
Docker lets you run the same labs locally without a full VM. Install Docker Desktop for macOS:

```bash
brew install --cask docker
# Then open Docker.app from Applications to finish setup.
```

Start Docker and confirm it runs:

```bash
docker --version
docker run --rm hello-world
```

## 4) Option A — Lightweight VM: Multipass (recommended for Ubuntu VM)
Multipass quickly launches Ubuntu instances for hands-on Linux work.

```bash
brew install --cask multipass
# Launch an Ubuntu VM
multipass launch --name ubuntu-lab --mem 2G --disk 10G
# Connect to the VM
multipass shell ubuntu-lab
```

Inside the VM you will be in a native Ubuntu shell. Use `exit` to leave.

## 4b) Option B — Full VM: VirtualBox + Ubuntu (alternate)
If you prefer a traditional VM, install VirtualBox and the Ubuntu Desktop/Server image.

```bash
brew install --cask virtualbox
# Download Ubuntu from https://ubuntu.com/download and create a new VM using VirtualBox UI
```

## 5) Create a Linux user and set up SSH (inside a VM)
Inside your Ubuntu VM (Multipass shell or VirtualBox):

```bash
# add a new user (replace alice)
sudo adduser alice
sudo usermod -aG sudo alice
```

To connect from your macOS host using SSH (multipass example):

```bash
multipass info ubuntu-lab  # shows IP
ssh ubuntu@<VM_IP>
```

## 6) Useful Homebrew packages for the course

```bash
brew install git pyenv coreutils jq
```

## 7) Quick verification (on macOS)

```bash
# check basic commands
bash --version
git --version
docker --version
multipass version  # if installed
```

## Troubleshooting
- If `docker` commands fail, open Docker Desktop and allow required permissions.
- If Multipass fails to launch VMs, check macOS virtualization settings (Apple Silicon vs Intel differences) and use the VirtualBox option if needed.

## Notes for learners
- You do not need a VM for every lesson — many commands run on macOS directly. Use a VM when the lab requires a Linux environment (packages, services, systemd, etc.).

---

If you want, I can also add a small script to automate creating a Multipass VM and installing common packages for students.
Use VirtualBox/VMware to run Ubuntu for full Linux experience
