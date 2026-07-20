from __future__ import annotations

from typing import Literal

_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_BASE = len(_ALPHABET)


class Base62Codec:
    """Encode and decode raw bytes or UTF-8 text using Base62."""

    alphabet = _ALPHABET

    @classmethod
    def encode(cls, data: bytes | str, encoding: str = "utf-8") -> str:
        """Encode bytes or text to a Base62 string."""
        if isinstance(data, str):
            data = data.encode(encoding)

        if len(data) == 0:
            return ""

        leading_zeros = 0
        for byte in data:
            if byte == 0:
                leading_zeros += 1
            else:
                break

        value = int.from_bytes(data, "big")
        encoded = cls._encode_int(value)
        return cls.alphabet[0] * leading_zeros + encoded

    @classmethod
    def decode(cls, text: str, decode_as: Literal["bytes", "text"] = "bytes", encoding: str = "utf-8") -> bytes | str:
        """Decode a Base62 string to bytes or text."""
        if text == "":
            result = b""
        else:
            leading_zeros = 0
            for char in text:
                if char == cls.alphabet[0]:
                    leading_zeros += 1
                else:
                    break

            remainder = text[leading_zeros:]
            value = cls._decode_int(remainder) if remainder else 0
            decoded = value.to_bytes((value.bit_length() + 7) // 8, "big")
            result = b"\x00" * leading_zeros + decoded

        if decode_as == "text":
            return result.decode(encoding)
        return result

    @classmethod
    def _encode_int(cls, value: int) -> str:
        if value == 0:
            return cls.alphabet[0]

        result_chars: list[str] = []
        while value > 0:
            value, remainder = divmod(value, _BASE)
            result_chars.append(cls.alphabet[remainder])
        return "".join(reversed(result_chars))

    @classmethod
    def _decode_int(cls, text: str) -> int:
        value = 0
        for char in text:
            index = cls.alphabet.index(char)
            value = value * _BASE + index
        return value
