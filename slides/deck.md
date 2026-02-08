---
title: Linux Zero to Hero — Slide Deck
author: Course
theme: beige
revealOptions:
  center: true
  transition: slide
---

# Linux Zero to Hero

Welcome — quick orientation and learning path. This deck uses short stories, interactive prompts, and micro-quizzes to keep learners engaged.

---

## Introduction

Get learners oriented quickly: what to expect and the recommended learning path.

- Open a terminal and run basic commands
- Understand filesystem layout and permissions
- Use common commands for files, processes, and networking
- Complete hands-on labs in the `labs/` folder

<aside class="notes">Tip for presenters: open with a 2-minute personal story about when a single command saved your day — this builds curiosity.</aside>

---

## Linux Basics

- What is Linux and where it runs
- Kernel vs userspace vs distributions
- Filesystem layout: `/`, `/etc`, `/var`, `/home`, `/usr`

Key demo: `ls -la`, `pwd`, `less`

![Architecture](assets/architecture.svg)

<aside class="notes">
Detailed notes — Linux Basics
- Spend 3 minutes explaining kernel vs userspace with the architecture image.
- Live demo: run `pwd` then `ls -la` in a sample repo. Explain columns in `ls -la` (permissions, links, owner, size, date, name).
- Encourage learners to create a directory and a file, then show `less` and `head` to inspect content.
- Audience prompt: "Which directory likely contains server logs?" (Reveal answer `/var/log` after a pause.)
</aside>

---

## Common Commands

- Files & directories: `ls`, `cp`, `mv`, `rm`, `find`
- Viewing & editing: `cat`, `less`, `head`, `tail`, `grep`
- Processes & services: `ps`, `top`, `systemctl`, `journalctl`
- Networking: `ip`, `ping`, `curl`, `ss`

Demo flow:
1. Create files and search with `find` + `grep`
2. Show process list and filter with `ps aux | grep`
3. Query a web endpoint with `curl`

<aside class="notes">
Detailed notes — Common Commands
- Demo 1 (files): `mkdir demo && cd demo && echo hello > note.txt && ls -la` then `find . -type f -name "*.txt"`.
- Demo 2 (viewing): `cat note.txt`, `less note.txt`, `head -n 3 note.txt`.
- Demo 3 (processes): `ps aux | head -n 10` then `ps aux | grep -i flask` (or other sample app).
- Demo 4 (network): `curl -I https://example.com` and explain HTTP response headers.
- Micro-challenge: "Find the file named 'secret.txt' in under 60 seconds." If learners struggle, hint: `find . -name secret.txt`.
</aside>

---

## Practice & Labs

- Run the `labs/` Docker environment
- Beginner tasks: create files, inspect logs, fix permissions
- Intermediate: use `tar`/`gzip`, deploy the provided Flask app

Session structure:
1. Live demo (8–10 minutes)
2. Quick story-driven challenge (10–15 minutes)
3. Guided exercise (15–20 minutes)
4. Review & micro-quiz (5–10 minutes)

<aside class="notes">
Detailed notes — Practice & Labs
- Prep step: remind learners to run `labs/start.sh` and open the demo app URL shown by Docker Compose.
- Demo: tail the app log (e.g., `tail -f labs/logs/myapp.log`) and reproduce a small error by calling a specific endpoint.
- Guided exercise: give step-by-step checklist in chat and let learners pair-program for 15 minutes.
- Safety note: all destructive operations should be performed inside the `labs/` Docker environment only.
</aside>

---

## Scenarios (Quick)

- Server down: check processes, Nginx, and app logs
- Disk full: identify large files and clean safely
- High CPU: identify offending process
- Permission denied: fix ownership and permissions

Checklist: `journalctl -u <service>`, `du -sh`, `top`

---

## Story: The 502 Mystery (mini-case)

Our storefront shows a 502 error at 09:12. Customers report timeouts. What do you check first?

- Step 1: Check Nginx logs
- Step 2: Check upstream app logs
- Step 3: Check disk space and process health

<aside class="notes">Walk learners through `tail -n 200 /var/log/nginx/error.log`, `docker-compose logs app`, and `df -h`. Emphasize method over magic commands.</aside>

<aside class="notes">
Extended walkthrough — The 502 Mystery
1) Show Nginx error log and highlight a 502 entry (explain upstream timeout vs bad gateway).
2) Check upstream app logs for exceptions or worker crashes; show `docker-compose logs app --tail=200`.
3) Confirm system health: `df -h` and `top` to ensure resources are available.
4) If the app crashed due to missing env var, demonstrate safe restart and inspect `systemctl` / process manager if outside Docker.
</aside>

---

## Micro-quiz: Quick check

What command shows which process owns port 80?

- A) `ps aux`
- B) `ss -tulpn`
- C) `netstat -an`

---

## Micro-quiz: Answer

Correct: B) `ss -tulpn`

<aside class="notes">Explain why `ss -tulpn` is preferred (shows pid/program and is available on modern systems).</aside>

---

## Resources & Cheat Sheets

- Files & permissions: `ls -l`, `chmod`, `chown`
- Processes: `ps`, `top`, `systemctl`, `journalctl`
- Disk & network: `df -h`, `du -sh`, `ip addr`, `ss -tulpn`

Man pages: `man <command>` — Practice using `labs/` exercises.

---

## Interactive Challenge (classroom)

Task: In the `labs/` environment, reproduce a disk-full scenario safely: create a 100MB temp file, find it with `du`, and delete it. Timebox to 6 minutes.

Hints:
- Use `fallocate` or `dd` to create a file
- Use `du -sh` and `find` to locate large files

<aside class="notes">This challenge is repeatable and safe when done in the provided Docker labs; remind learners not to run destructive commands on production systems.</aside>

![Terminal Demo](assets/terminal.svg)

<aside class="notes">
Instructor tips for the Interactive Challenge
- Use `fallocate -l 100M /tmp/bigfile` (or `dd if=/dev/zero of=/tmp/bigfile bs=1M count=100`) to create a test file.
- Use `du -sh /tmp/* | sort -hr | head -n 10` to locate large files.
- After deleting the file, show `sync` and `df -h` again to explain filesystem behavior (note: some files still held by processes until closed).
</aside>

---

## Next steps

- Follow the suggested path in the repo: `installation/` → `linux-basics/` → `linux-commands/` → `practice/` → `scenarios/`
- Use `slides/deck.md` with `reveal-md` or `pandoc` to present.

<aside class="notes">Close with a short reflection prompt: "Which command from today will you use tomorrow?" and collect 3 answers from the audience.</aside>
