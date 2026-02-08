# Linux Zero to Hero — Friendly, Practical, Start-to-Finish

This repository is a complete, beginner-first Linux course designed so anyone — even without an IT background — can learn Linux from zero and reach practical, job-ready skills.

Why this course works: short explanations, real-world examples, step-by-step commands, and hands-on exercises so concepts click quickly and stay interesting.

---

**Quick promise:** after following the first few folders you will be able to open a terminal, run the basic commands, and understand what a Linux server looks like and why each step matters.

---

## What you'll learn (short)
- Understand what Linux is and where it runs (servers, laptops, cloud)
- Navigate the filesystem and manage files and permissions
- Run and combine everyday commands with real examples
- Install software and manage packages
- Monitor processes, disk, and network health
- Troubleshoot common server problems using scenarios
- Automate simple tasks with shell scripts (advanced sections)

---

## Getting started — No prior IT knowledge needed

1. Open a terminal (macOS: Terminal app, Windows: WSL terminal, or use a cloud VM).
2. Try these first, and read the short explanation after each command.

```bash
# show current folder path
pwd

# list files (short) with human-readable sizes
ls -lh

# show who you are (username) and machine name
whoami && hostname

# show first 10 lines of this README (if you're in the repo folder)
head -n 10 README.md
```

What to expect from outputs:
- `pwd` prints the current folder (your place in the system).
- `ls -lh` shows files with sizes you can read (K, M), no mystery numbers.
- `whoami` & `hostname` show who you are on the system and which machine you're on.
- `head` previews files so you don't accidentally open large files.

If something looks different, that's okay — we'll show examples for macOS, WSL (Windows), and a simple Linux VM later.

---

## How this repo is organized (what to open first)
- `installation/` — Setup guides for Windows WSL, VirtualBox, and macOS. Start here if you don't have a Linux environment.
- `linux-basics/` — Friendly, plain-language lessons: What is Linux, architecture, and the filesystem.
- `linux-commands/` — Practical command-by-command guide with examples, expected outputs, and real tasks.
- `practice/` — Hands-on exercises with step-by-step solutions and hints.
- `scenarios/` — Real-world problems (server down, disk full) with walkthroughs and commands used to fix them.
- `resources/` — Cheat sheets, interview questions, and extra reading.
- `slides/` — Slide material and lesson notes (useful for quick review).

Start here if you're new: `installation/` → `linux-basics/01-what-is-linux.md` → `linux-commands/01-file-directory-commands.md` → `practice/01-beginner-tasks.md`.

---

## Teaching style & examples
- Every command has: what it does, a short example, expected output, and a real-world story (why you'd use it).
- Exercises are bite-sized: 5–10 minutes each, with hints and full solutions.
- Scenarios are realistic: production-style problems with safe, repeatable steps.

Example lesson excerpt (from `linux-commands/01-file-directory-commands.md`):

```text
Problem: You uploaded a file to a server and can’t find it.
Command: ls -lah /path/to/check
Why: Lists hidden files and long details so you can see permissions and sizes.
Real output: shows the file with size & owner — now you can `cat` or `less` it.
```

---

## How to use this repo day-by-day (suggested path)
- Day 1: Setup (`installation/`), open terminal, run the quick commands above.
- Day 2–4: `linux-basics/` (read with hands-on follow-along).
- Day 5–8: `linux-commands/` — do 10 commands per day and try short exercises.
- Week 2: `practice/` and `scenarios/` — apply what you've learned to realistic problems.

---

---

Made for learners who want clarity, real examples, and fast progress.

Good luck — and tell me which lesson to build next!
