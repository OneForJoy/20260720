#!/usr/bin/env python3
"""Standalone ASGI server wrapper for Base62 FastAPI app."""

import asyncio
import socket
import sys
from app import app


async def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run the ASGI app using a custom async server."""
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    config.bind = [f"{host}:{port}"]
    config.loglevel = "warning"

    print(f"🚀 Starting server on http://{host}:{port}")
    print(f"   OpenAPI docs: http://{host}:{port}/docs")
    print(f"   Press Ctrl+C to quit\n")

    try:
        await serve(app, config)
    except KeyboardInterrupt:
        print("\n✅ Server stopped")


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000

    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    asyncio.run(run_server(host, port))
