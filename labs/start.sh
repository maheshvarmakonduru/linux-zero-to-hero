#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
docker-compose up --build -d
echo "Lab started. Visit http://localhost:8080 and tail app logs: tail -f app/logs/app.log"
