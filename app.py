from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from base62_codec import Base62Codec


class EncodeRequest(BaseModel):
    input: str
    text: bool = True


class EncodeResponse(BaseModel):
    base62: str


class DecodeRequest(BaseModel):
    input: str
    text: bool = False
    raw: bool = False


class DecodeResponse(BaseModel):
    result: str
    raw_hex: str | None = None


app = FastAPI(
    title="Base62 Codec API",
    description="Encode and decode data with Base62 using a FastAPI service.",
    version="0.1.0",
)


@app.get("/", summary="API status")
def root() -> dict[str, str]:
    return {"status": "ok", "service": "base62-codec"}


@app.post("/encode", response_model=EncodeResponse, summary="Encode text to Base62")
def encode(request: EncodeRequest) -> EncodeResponse:
    raw_input = request.input if request.text else request.input.encode("utf-8")
    encoded = Base62Codec.encode(raw_input)
    return EncodeResponse(base62=encoded)


@app.post("/decode", response_model=DecodeResponse, summary="Decode Base62 to text or hex")
def decode(request: DecodeRequest) -> DecodeResponse:
    decoded = Base62Codec.decode(request.input, decode_as="text" if request.text else "bytes")

    if request.raw:
        raw_hex = Base62Codec.decode(request.input, decode_as="bytes").hex()
        return DecodeResponse(result=decoded if request.text else "", raw_hex=raw_hex)

    return DecodeResponse(result=decoded if request.text else decoded.hex(), raw_hex=None)
