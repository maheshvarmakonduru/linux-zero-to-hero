# Install Linux on Windows Using WSL

WSL = Windows Subsystem for Linux → lets you run Linux inside Windows.

**Steps:**
1. Open PowerShell as Administrator
2. Run:
   ```bash
   wsl --install
   ```
3. Restart Windows
4. Set Linux username & password
5. Run wsl --list --verbose to verify

**Recommended Distro:** Ubuntu LTS

**Example:**
After WSL installation, you can run Linux commands like ls, top, df -h directly in Windows terminal.
