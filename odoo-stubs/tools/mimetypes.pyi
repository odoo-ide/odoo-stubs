from collections import namedtuple
from typing import Any

__all__: Any
_logger: Any
_ooxml_dirs: Any

def _check_ooxml(data): ...

_mime_validator: Any

def _check_open_container_format(data): ...

_xls_pattern: Any
_ppt_pattern: Any

def _check_olecf(data): ...
def _check_svg(data): ...

_Entry = namedtuple("_Entry", ["mimetype", "signatures", "discriminants"])
_mime_mappings: Any

def guess_mimetype(bin_data, default: str = ...): ...

guess_mimetype: Any
ms: Any
