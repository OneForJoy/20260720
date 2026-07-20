from __future__ import annotations

import argparse
import sys

from base62_codec import Base62Codec


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="base62-codec")
    subparsers = parser.add_subparsers(dest="command", required=True)

    encode_parser = subparsers.add_parser("encode", help="Encode bytes or text to Base62")
    encode_parser.add_argument("input", help="Input text or bytes to encode")
    encode_parser.add_argument("--text", action="store_true", help="Treat input as UTF-8 text")

    decode_parser = subparsers.add_parser("decode", help="Decode Base62 to bytes or text")
    decode_parser.add_argument("input", help="Base62 string to decode")
    decode_parser.add_argument("--raw", action="store_true", help="Return raw bytes as hex")
    decode_parser.add_argument("--text", action="store_true", help="Decode output as UTF-8 text")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "encode":
        data = args.input if args.text else args.input.encode("utf-8")
        encoded = Base62Codec.encode(data) if args.text else Base62Codec.encode(data)
        print(encoded)
        return 0

    if args.command == "decode":
        decoded = Base62Codec.decode(args.input, decode_as="text" if args.text else "bytes")
        if args.text:
            print(decoded)
            return 0
        print(decoded.hex())
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
