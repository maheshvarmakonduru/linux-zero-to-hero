```markdown
# Scenarios — Slides

## Scenario list (quick)
- Server down: check processes, Nginx, and app logs
- Disk full: identify large files and clean safely
- High CPU: identify offending process and investigate
- Permission denied: fix ownership and permissions safely

## Demo checklist
- Show `journalctl -u <service>` for service logs
- Use `du -sh` to find large directories
- Use `top`/`htop` to spot CPU usage

```
