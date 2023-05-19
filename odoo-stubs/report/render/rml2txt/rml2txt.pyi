from typing import Any

Font_size: float

def verbose(text) -> None: ...

class textbox:
    posx: Any
    posy: Any
    lines: Any
    curline: str
    endspace: bool
    def __init__(self, x: int = ..., y: int = ...) -> None: ...
    def newline(self) -> None: ...
    def fline(self) -> None: ...
    def appendtxt(self, txt) -> None: ...
    def rendertxt(self, xoffset: int = ...): ...
    def renderlines(self, pad: int = ...): ...
    def haplines(self, arr, offset, cc: str = ...) -> None: ...

def parseNode(
    rml,
    localcontext: Any | None = ...,
    fout: Any | None = ...,
    images: Any | None = ...,
    path: str = ...,
    title: Any | None = ...,
): ...
def parseString(
    rml,
    localcontext: Any | None = ...,
    fout: Any | None = ...,
    images: Any | None = ...,
    path: str = ...,
    title: Any | None = ...,
): ...
def trml2pdf_help() -> None: ...
