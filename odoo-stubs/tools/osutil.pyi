import ctypes
from typing import Any

_logger: Any
WINDOWS_RESERVED: Any

def clean_filename(name, replacement: str = ...): ...
def listdir(dir, recursive: bool = ...): ...
def walksymlinks(top, topdown: bool = ..., onerror: Any | None = ...): ...
def tempdir() -> None: ...
def zip_dir(path, stream, include_dir: bool = ..., fnct_sort: Any | None = ...) -> None: ...

getppid: Any
is_running_as_nt_service: Any
_TH32CS_SNAPPROCESS: int

class _PROCESSENTRY32(ctypes.Structure):
    _fields_: Any
