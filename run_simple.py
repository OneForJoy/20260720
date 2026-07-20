#!/usr/bin/env python3
"""Simple ASGI to WSGI adapter server for Base62 FastAPI."""

import sys
from app import app


if __name__ == "__main__":
    import uvicorn
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    
    # Use threading instead of async to avoid Windows socket issues
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="warning",
        loop="asyncio"  # Explicitly use asyncio loop
    )
