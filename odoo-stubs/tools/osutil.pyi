from re import Pattern
from typing import BinaryIO, Callable, Iterable

WINDOWS_RESERVED: Pattern

def clean_filename(name: str, replacement: str = ...) -> str: ...
def listdir(dir: str, recursive: bool = ...) -> Iterable[str]: ...
def zip_dir(
    path: str,
    stream: str | BinaryIO,
    include_dir: bool = ...,
    fnct_sort: Callable | None = ...,
) -> None: ...

is_running_as_nt_service: Callable[[], bool]
