from typing import Any

from reportlab import platypus
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import ActionFlowable

encoding: str

def select_fontname(fontname, default_fontname): ...

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs) -> None: ...
    def showPage(self) -> None: ...
    def save(self) -> None: ...
    def draw_page_number(self) -> None: ...

class PageCount(platypus.Flowable):
    story_count: Any
    def __init__(self, story_count: int = ...) -> None: ...
    def draw(self) -> None: ...

class PageReset(platypus.Flowable):
    def draw(self) -> None: ...

original_pto_split: Any

def split(self, availWidth, availHeight): ...

class EndFrameFlowable(ActionFlowable):
    def __init__(self, resume: int = ...) -> None: ...

class TinyDocTemplate(platypus.BaseDocTemplate):
    def beforeDocument(self) -> None: ...
    frame: Any
    page: int
    def afterPage(self) -> None: ...

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
