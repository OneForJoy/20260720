# Base62 Codec

A minimal Python 3.14 project that encodes arbitrary data into Base62 and decodes it back exactly.

## Features

- Encode bytes or UTF-8 strings to Base62
- Decode Base62 back to bytes or text
- Preserves leading zero bytes and empty input
- Managed via `uv` for Python environment and execution

## Install

```powershell
uv install
```

## Run the FastAPI service

```powershell
uv run serve
```

The API will be available at `http://127.0.0.1:8000`.

## FastAPI endpoints

- `GET /` - service status
- `POST /encode` - encode text to Base62
- `POST /decode` - decode Base62 to text or raw hex

Example request body for `/encode`:

```json
{
	"input": "hello world",
	"text": true
}
```

Example request body for `/decode`:

```json
{
	"input": "AAwf93rvy4aWQVw",
	"text": true
}
```

## Usage

Encode a UTF-8 string:

```powershell
uv run python -m base62_codec encode "hello world"
```

Decode a Base62 value to text:

```powershell
uv run python -m base62_codec decode "0Z3KxXMh"
```

Decode to raw bytes:

```powershell
uv run python -m base62_codec decode --raw "0Z3KxXMh"
```

## Run tests

```powershell
uv run python -m pytest
```
