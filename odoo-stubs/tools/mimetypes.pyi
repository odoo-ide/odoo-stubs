from collections import namedtuple
from typing import Any

__all__: Any
_logger: Any
_ooxml_dirs: Any

def _check_ooxml(data: Any): ...

_mime_validator: Any

def _check_open_container_format(data: Any): ...

_xls_pattern: Any
_ppt_pattern: Any

def _check_olecf(data: Any): ...
def _check_svg(data: Any): ...

_Entry = namedtuple('_Entry', ['mimetype', 'signatures', 'discriminants'])
_mime_mappings: Any

def guess_mimetype(bin_data: Any, default: str = ...): ...

guess_mimetype: Any
ms: Any

def neuter_mimetype(mimetype: Any, user: Any): ...
