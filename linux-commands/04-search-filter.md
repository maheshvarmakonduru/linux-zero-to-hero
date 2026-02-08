# Search & Filter Commands

**Search inside files:**
- `grep -n "pattern" file` — find lines that match and show line numbers.
	- Example: `grep -n "ERROR" /var/log/nginx/error.log`

**Find files by name:**
- `find /path -type f -name "*.log" -maxdepth 3 -print`
	- Example: `find ~ -type f -name "*.log" -maxdepth 3 -print`

**Advanced:**
- `awk '{print $1}' file` — print first column (useful for structured text).
- `sed 's/old/new/g' file` — simple find-and-replace (useful in scripts).
- `sort`, `uniq -c`, `cut` are useful together: `cat file | cut -d',' -f2 | sort | uniq -c`.

**Scenario:**  
Find all error messages in logs:
```bash
cat access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 5
```

Exercise (5–10 minutes)

1. Search this repository for the word "exercise" and show the filenames.
2. Find all `.md` files in this repo and count them.

Hints:
```bash
grep -Rni "exercise" .
find . -type f -name "*.md" | wc -l
```

Where to go next

- After filtering and searching, move to `linux-commands/02-file-viewing-editing.md` to practice viewing the files you find.
```
