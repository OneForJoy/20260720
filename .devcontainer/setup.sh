#!/usr/bin/env bash
set -e

echo "[SETUP] Updating apt packages..."
sudo apt-get update -y

echo "[SETUP] Installing Webtop dependencies..."
sudo apt-get install -y \
    curl wget git \
    net-tools dnsutils \
    python3-venv python3-pip

echo "[SETUP] Installing Poetry..."
curl -sSL https://install.python-poetry.org | python3 -

echo "[SETUP] Installing project dependencies..."
if [ -f "pyproject.toml" ]; then
    ~/.local/bin/poetry install || true
fi

echo "[SETUP] Setup complete."
