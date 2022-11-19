import collections
from re import Pattern
from typing import Any, Literal

__all__ = ['guess_mimetype']
_ooxml_dirs: dict[str, str]

def _check_ooxml(data: bytes) -> str | Literal[False]: ...

_mime_validator: Pattern

def _check_open_container_format(data: bytes) -> str | Literal[False]: ...

_xls_pattern: Pattern
_ppt_pattern: Pattern

def _check_olecf(data: bytes) -> str | Literal[False]: ...
def _check_svg(data: bytes) -> str | None: ...

_Entry = collections.namedtuple('_Entry', ['mimetype', 'signatures', 'discriminants'])
_mime_mappings: tuple[_Entry, ...]

def guess_mimetype(bin_data: str, default: str | None = ...) -> str: ...

_guesser: Any
ms: Any

def get_extension(filename: str) -> str: ...
