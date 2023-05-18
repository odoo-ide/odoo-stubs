from os import R_OK as R_OK
from os import W_OK as W_OK
from os.path import dirname as dirname
from typing import Any

__docformat__: str
__all__: Any
windows: Any
seen: Any
defpathext: Any

def which_files(
    file, mode=..., path: Any | None = ..., pathext: Any | None = ...
) -> None: ...
def which(file, mode=..., path: Any | None = ..., pathext: Any | None = ...): ...
