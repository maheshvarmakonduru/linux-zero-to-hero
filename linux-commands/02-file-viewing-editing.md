# File Viewing & Editing — read and change files safely

Viewing files

- `cat file` — print the whole file (good for small files).
- `head -n 10 file` — show the first 10 lines.
- `tail -n 10 file` — show the last 10 lines.
- `tail -f file` — follow a growing file (useful for logs).
- `less file` — scrollable viewer; press `q` to quit.

Examples:

```bash
head -n 20 README.md
tail -n 50 /var/log/syslog
tail -f /var/log/nginx/access.log
less /var/log/nginx/error.log
```

Searching file contents

- `grep -n "pattern" file` — search for `pattern` and show line numbers.
- Combine with `pipe` to filter output: `dmesg | grep -i usb`.

Editing files

- `nano file` — simple, beginner-friendly text editor.
- `vim file` — powerful editor (has learning curve).

Redirection and pipes (quick notes)

- `>` writes output to a file (overwrites): `echo hello > file.txt`
- `>>` appends: `echo more >> file.txt`
- `|` pipes output to next command: `cat file | grep foo`

Safety tips

- Use `less` or `head` before editing to inspect large files.
- When editing system files (in `/etc`), make a backup first: `sudo cp /etc/my.conf /etc/my.conf.bak`.

Exercise (5–10 minutes)

1. Use `head` and `tail` to view the first and last 5 lines of `README.md`.
2. Search this repository for the word "exercise": `grep -Rni "exercise" .`

Solution hints:

```bash
head -n 5 README.md
tail -n 5 README.md
grep -Rni "exercise" .
```

Where to go next

- Next: `linux-commands/03-permissions-ownership.md` to learn who can read and write files and how to change that safely.
