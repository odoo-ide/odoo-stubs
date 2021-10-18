from typing import Any, NamedTuple

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

class _Entry(NamedTuple):
    mimetype: Any
    signatures: Any
    discriminants: Any
_mime_mappings: Any

def _odoo_guess_mimetype(bin_data, default: str = ...): ...

_guesser: Any
ms: Any

def guess_mimetype(bin_data, default: Any | None = ...): ...
guess_mimetype = _odoo_guess_mimetype

def neuter_mimetype(mimetype, user): ...
