from base62_codec import Base62Codec


def test_encode_decode_round_trip_bytes() -> None:
    data = b"\x00\x01\x02hello\x00"
    encoded = Base62Codec.encode(data)
    decoded = Base62Codec.decode(encoded)

    assert decoded == data


def test_encode_decode_round_trip_text() -> None:
    text = "Hello, Base62!"
    encoded = Base62Codec.encode(text)
    decoded = Base62Codec.decode(encoded, decode_as="text")

    assert decoded == text


def test_empty_bytes() -> None:
    assert Base62Codec.encode(b"") == ""
    assert Base62Codec.decode("") == b""


def test_encode_leading_zero_bytes() -> None:
    data = b"\x00\x00abc"
    encoded = Base62Codec.encode(data)
    assert encoded.startswith("00")
    assert Base62Codec.decode(encoded) == data
