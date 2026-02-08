# File & Directory Commands

**Navigation:**
- `pwd` → show current directory
- `cd /path/to/folder` → change directory

**Listing Files:**
- `ls` → list files
- `ls -la` → detailed view including hidden files

**Creating & Deleting:**
- `mkdir folder` → create directory
- `touch file` → create file
- `rm file` → delete file
- `rm -rf folder` → delete folder recursively

**Example:**  
Deleting old logs:
# File & Directory Commands — beginner friendly

This lesson covers the everyday commands you will use to move around the filesystem, inspect files, and create or remove items. Each command includes a simple explanation, a realistic example, and a short note about safety or a common pitfall.

Navigation

- `pwd` — print working directory
	- What it does: shows the full path of your current folder.
	- Example:
		```bash
		pwd
		/home/mahesh/projects/linux-zero-to-hero
		```

- `cd <path>` — change directory
	- What it does: move to another folder. `cd` with no arguments goes to your home folder.
	- Examples:
		```bash
		cd /var/log
		cd ~/projects/linux-zero-to-hero
		cd ..    # go up one level
		```

Listing files

- `ls` — list files and folders
	- Basic use: `ls` shows names; `ls -l` shows details; `ls -lh` shows human-readable sizes (K/M/GB).
	- Example:
		```bash
		ls -lh
		total 12K
		-rw-r--r-- 1 mahesh staff 1.2K Feb  8 10:00 README.md
		drwxr-xr-x 3 mahesh staff 4.0K Feb  8 09:00 linux-basics
		```

- `ls -la` — show hidden files and full details
	- Hidden files start with `.`. This is useful when configuration files are not visible by default.
	- Example:
		```bash
		ls -la
		drwxr-xr-x 5 mahesh staff 160 Feb  8 09:00 .
		-rw-r--r-- 1 mahesh staff  18 Feb  8 09:01 .gitignore
		```

Inspecting files and quick previews

- `cat file` — print the full file to the terminal (useful for small files)
	- Example: `cat README.md`

- `head -n 10 file` / `tail -n 10 file` — show start or end of a file
	- Use `less file` to scroll a long file interactively.

- `file filename` — tells you the file type (text, executable, image)
	- Example: `file script.sh` → `script.sh: ASCII text executable`

Create, copy, move, delete

- `mkdir folder` — create a folder
	- Example: `mkdir projects/my-new-course`

- `touch file` — create an empty file or update its timestamp
	- Example: `touch notes.txt`

- `cp source dest` — copy files
	- Example: `cp notes.txt notes.bak`

- `mv source dest` — move or rename
	- Example: `mv notes.bak archive/` or `mv oldname.txt newname.txt`

- `rm file` — delete a file
	- Safety: deleted files are usually not recoverable. Use `rm` carefully.
	- Example: `rm temp.txt`

- `rm -rf folder` — delete a folder and everything inside
	- Danger: this is destructive. Always double-check the path. Consider listing the folder first: `ls -la /path/to/folder`
	- Safer alternative for interactive deletion: `rm -ri folder` (prompts before each removal).

Useful real-world examples

- Find a file by name and show its directory:
	```bash
	find ~ -type f -name "*.log" -maxdepth 3 -print
	/home/mahesh/app/logs/error.log
	```

- Search inside files for a term and show matching lines:
	```bash
	grep -n "ERROR" /var/log/syslog
	142:Feb  8 10:12:02 myserver app[123]: ERROR: connection refused
	```

- Quickly check disk usage of a folder (human-readable):
	```bash
	du -sh /var/log
	120M   /var/log
	```

Common pitfalls and tips

- If `ls` shows fewer files than you expect, use `ls -la` to reveal hidden files.
- Always confirm the path before `rm -rf`. A common safe habit: run `pwd` and `ls` first.
- Use `--help` or `man` pages: `ls --help` or `man ls` to learn more about options.

Short practice exercises (10–15 minutes)

Exercise 1 — Create and inspect

1. Create a folder `learning-day1` and enter it.
2. Create three files inside it: `notes.txt`, `todo.md`, `example.log` (use `touch`).
3. List files with details and create a backup copy of `notes.txt` named `notes.bak`.

Hints:
```bash
mkdir learning-day1
cd learning-day1
touch notes.txt todo.md example.log
ls -lh
cp notes.txt notes.bak
```

Solution (what success looks like):
```text
drwxr-xr-x 2 mahesh staff 4.0K Feb  8 10:40 .
-rw-r--r-- 1 mahesh staff    0 Feb  8 10:40 example.log
-rw-r--r-- 1 mahesh staff    0 Feb  8 10:40 notes.bak
-rw-r--r-- 1 mahesh staff    0 Feb  8 10:40 notes.txt
-rw-r--r-- 1 mahesh staff    0 Feb  8 10:40 todo.md
```

Exercise 2 — Find and clean

1. Use `find` to locate files named `*.log` starting from your home directory (limit depth to 3).
2. If you find a log file that is larger than 50M, print its name and size using `du -h`.

Hints:
```bash
find ~ -type f -name "*.log" -maxdepth 3 -print
du -h /path/to/found.log
```

What to do if you make a mistake

- If you accidentally remove a file and you have backups (e.g., in `notes.bak`), restore from the backup with `cp notes.bak notes.txt`.
- If this is a production server with no backups, stop using the disk immediately and contact a system administrator — data recovery may be possible but is outside the scope of this lesson.

Where to go next

- After you're comfortable with these commands, continue to `linux-commands/02-file-viewing-editing.md` to learn how to read and edit files safely.
