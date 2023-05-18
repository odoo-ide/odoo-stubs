from typing import Any

class SourceMapGenerator:
    _file: None
    _source_root: str | None
    _sources: dict[str, int]
    _mappings: list[dict[str, Any]]
    _sources_contents: dict[str, str]
    _version: int
    _cache: dict[tuple[int, int], str]
    def __init__(self, source_root: str | None = ...) -> None: ...
    def _serialize_mappings(self) -> str: ...
    def to_json(self) -> dict: ...
    def get_content(self) -> bytes: ...
    def add_source(
        self,
        source_name: str,
        source_content: str,
        last_index: int,
        start_offset: int = ...,
    ) -> None: ...

B64CHARS: bytes
SHIFTSIZE: int
FLAG: int
MASK: int

def base64vlq_encode(*values) -> str: ...
