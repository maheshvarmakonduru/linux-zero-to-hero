# Intermediate Practice

# Intermediate Practice — build practical troubleshooting skills

Exercise 1 — Search and summarize logs (10 minutes)

1. Search `/var/log` for the word "ERROR" and save matches to `errors.txt`.
2. Count how many distinct files contain errors.

Hints:
```bash
grep -Rni "ERROR" /var/log | tee errors.txt
cut -d: -f1 errors.txt | sort -u | wc -l
```

Exercise 2 — Monitor and capture process info (10 minutes)

1. Run `top` or `htop` and identify a process consuming CPU.
2. Save a snapshot of running processes to `process-snapshot.txt`.

Hints:
```bash
ps aux --sort=-%cpu | head -n 20 > process-snapshot.txt
top -b -n1 | head -n 30 >> process-snapshot.txt
```

Exercise 3 — Archive and verify (10 minutes)

1. Create a folder `backup-test` with a few files and compress it.
2. Verify the archive contents without extracting.

Commands:
```bash
mkdir backup-test && echo hi > backup-test/a.txt && echo bye > backup-test/b.txt
tar -czvf backup-test.tar.gz backup-test
tar -tzvf backup-test.tar.gz
```

Exercise 4 — Find large files (10 minutes)

1. Find files larger than 50M in your home directory (limit depth if needed).

Hints:
```bash
find ~ -type f -size +50M -exec ls -lh {} \; 2>/dev/null
```

Where to go next

- After these exercises, try `practice/03-advanced-tasks.md` to automate and scale these checks.
