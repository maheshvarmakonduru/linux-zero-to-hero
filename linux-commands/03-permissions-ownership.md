# Permissions & Ownership

**View permissions:**
```bash
ls -l
# File Ownership & Permissions — who can do what

Permissions control who can read, write or run a file. This prevents accidental or malicious changes.

Quick concepts

- `r` = read, `w` = write, `x` = execute
- Three classes: owner (user), group, others
- `ls -l` shows permissions, owner and group

Common commands with examples

- `ls -l filename`
	- Example output: `-rw-r--r-- 1 alice dev 1.2K Feb 8 10:00 notes.txt`

- `chmod 755 script.sh` — user: rwx, group: r-x, others: r-x
	- Symbolic example: `chmod u=rwx,g=rx,o=rx script.sh`

- `chown bob:admins file.txt` — change owner and group

- `chmod -R 750 folder/` — change permissions recursively for a folder

Numeric mode quick guide

- 4 = r, 2 = w, 1 = x. Add them for each class: `chmod 644 file` → owner rw, group r, others r.

Special bits

- `chmod +x file` — make script executable.
- `chmod 1777 /tmp` — sticky bit on shared folders (users can only delete their own files).

Safety tips

- Avoid `chmod 777` — it gives all permissions to everyone.
- Use `ls -l` before changing permissions to understand current state.

Exercise (5 minutes)

1. Create a file `secret.txt` and set permissions so only the owner can read/write.
2. Create `runme.sh` and make it executable.

Hints:
```bash
touch secret.txt
chmod 600 secret.txt
touch runme.sh
chmod +x runme.sh
```

Where to go next

- Continue to `linux-commands/05-process-management.md` to use permissions when starting services and scripts.
