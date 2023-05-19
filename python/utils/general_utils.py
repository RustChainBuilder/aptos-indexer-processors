import hashlib


def hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def truncate_str(s: str, max_len: int) -> str:
    if len(s) > max_len:
        return s[:max_len]
    else:
        return s


def standardize_address(address: str) -> str:
    address = address.removeprefix("0x")
    return "0x" + address.zfill(64)