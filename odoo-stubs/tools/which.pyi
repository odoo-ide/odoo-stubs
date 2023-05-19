from os import R_OK as R_OK
from os import W_OK as W_OK
from os.path import dirname as dirname
from typing import Iterator

ENOENT: int
windows: bool
seen: set
defpathext: list[str]

def which_files(
    file: str, mode: int = ..., path: str | None = ..., pathext: str | None = ...
) -> Iterator[str]: ...
def which(
    file: str, mode: int = ..., path: str | None = ..., pathext: str | None = ...
) -> str: ...
