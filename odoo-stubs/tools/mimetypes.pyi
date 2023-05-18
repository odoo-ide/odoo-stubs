from collections import namedtuple
from typing import Any

_Entry = namedtuple("_Entry", ["mimetype", "signatures", "discriminants"])

def guess_mimetype(bin_data, default: str = ...): ...

guess_mimetype: Any
