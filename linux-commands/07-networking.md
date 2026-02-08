# Networking Commands — check and troubleshoot connectivity

Interfaces and addresses

- `ip a` — show network interfaces and IP addresses
- `ip route` — show routing table (default gateway)

Connectivity checks

- `ping 8.8.8.8` — basic reachability test
- `traceroute example.com` — path packets take to a host
- `curl -I https://example.com` — view HTTP response headers

Ports and services

- `ss -tulnp` or `netstat -tulnp` — show listening sockets and owning process
- `nc -zv host port` — check if a TCP port is reachable

Copying files and remote access

- `scp file user@host:/path` — secure copy
- `rsync -avz local/ user@host:/path` — efficient sync and transfer
- `ssh user@host` — remote shell access

Quick example: check if a web server is listening locally

```bash
ss -tulnp | grep :80
curl -I http://localhost
```

Exercise (5–10 minutes)

1. Run `ip a` and note your active interface and IP address.
2. Use `curl -I https://example.com` to see HTTP headers.

Hints:
```bash
ip a
curl -I https://example.com
```

Where to go next

- Next: `linux-commands/08-package-management.md` to install tools used above (curl, traceroute, nc).
