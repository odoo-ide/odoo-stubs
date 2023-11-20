from re import Pattern
from typing import BinaryIO, Callable

WINDOWS_RESERVED: Pattern

def clean_filename(name: str, replacement: str = ...) -> str: ...
def zip_dir(
    path: str,
    stream: str | BinaryIO,
    include_dir: bool = ...,
    fnct_sort: Callable | None = ...,
) -> None: ...

is_running_as_nt_service: Callable[[], bool]
