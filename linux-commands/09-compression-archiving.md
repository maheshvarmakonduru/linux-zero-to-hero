# Compression & Archiving — save space and share folders

Tar and gzip (common for backups)

- Create compressed archive: `tar -czvf archive.tar.gz folder/`
- Extract: `tar -xzvf archive.tar.gz`

Zip (common on Windows)

- Create: `zip -r folder.zip folder/`
- Extract: `unzip folder.zip`

Examples

```bash
tar -cvf archive.tar folder/        # create uncompressed tar
gzip archive.tar                    # makes archive.tar.gz
tar -xzvf archive.tar.gz            # extract
```

Exercise (5 minutes)

1. Create a small folder with a couple of files and archive it with `tar` and `zip`.

Hints:
```bash
mkdir exercise-archive
echo hello > exercise-archive/a.txt
tar -czvf exercise.tar.gz exercise-archive
unzip -l exercise.tar.gz || true   # zip listing won't work on tar.gz; use tar -tzf
```

Where to go next

- Continue to `linux-commands/10-system-info.md` to gather system details useful for support tickets and debugging.
