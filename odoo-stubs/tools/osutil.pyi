from re import Pattern
from typing import Any, BinaryIO, Callable, Generator, Iterable, Iterator

WINDOWS_RESERVED: Pattern

def clean_filename(name: str, replacement: str = ...) -> str: ...
def listdir(dir: str, recursive: bool = ...) -> Iterable[str]: ...
def walksymlinks(
    top: str, topdown: bool = ..., onerror: Callable[[OSError], Any] | None = ...
) -> Iterator[tuple[str, list[str], list[str]]]: ...
def tempdir() -> Generator[str, None, None]: ...
def zip_dir(
    path: str,
    stream: str | BinaryIO,
    include_dir: bool = ...,
    fnct_sort: Callable | None = ...,
) -> None: ...

getppid: Callable[[], int]
is_running_as_nt_service: Callable[[], bool]
