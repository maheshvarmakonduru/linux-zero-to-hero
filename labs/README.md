# Labs — Run the course scenarios locally with Docker

This folder contains a small Docker-based lab that runs a demo `app` and an `nginx` reverse proxy. Use these labs to practice the scenarios in the course (service failures, logs, restarts, and basic troubleshooting) without affecting your main system.

Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic familiarity with running `docker-compose up`.

Quick start

1. Start the lab:

```bash
cd labs
docker-compose up --build -d
```

2. Visit `http://localhost:8080` to reach the demo site (nginx -> app).
3. View app logs:

```bash
tail -f app/logs/app.log
```

Useful lab actions

- Stop the lab:

```bash
docker-compose down
```

- Restart the app container:

```bash
docker-compose restart app
```

- Simulate an app crash (inside a separate terminal):

```bash
docker exec -it linux-zero-to-hero_app_1 pkill -f app.py || true
```

Notes

- Containers store logs in `labs/app/logs` on the host (shared volume) so you can inspect them directly.
- The lab is minimal by design — extend it to simulate DBs, disk full, or other services as needed.
