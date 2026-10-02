#!/usr/bin/env bash
set -e

echo "[WEBTOP] Starting Webtop container..."

docker rm -f webtop || true

docker run -d \
    --name webtop \
    --restart unless-stopped \
    -p 6080:3000 \
    --dns 8.8.8.8 \
    --dns 1.1.1.1 \
    --shm-size="2g" \
    lscr.io/linuxserver/webtop:debian-xfce

echo "[WEBTOP] Webtop is running on port 6080 with DNS enabled."
