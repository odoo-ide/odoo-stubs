from typing import Any

class SourceMapGenerator:
    _file: Any
    _source_root: Any
    _sources: Any
    _mappings: Any
    _sources_contents: Any
    _version: int
    _cache: Any
    def __init__(self, source_root: Any | None = ...) -> None: ...
    def _serialize_mappings(self): ...
    def to_json(self): ...
    def get_content(self): ...
    def add_source(self, source_name, source_content, last_index, start_offset: int = ...) -> None: ...

B64CHARS: bytes
SHIFTSIZE: Any
FLAG: Any
MASK: Any

def base64vlq_encode(*values): ...
