class SourceMapGenerator:
    def __init__(self, source_root: str | None = ...) -> None: ...
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
