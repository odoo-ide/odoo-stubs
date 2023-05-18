from typing import Any

from reportlab import platypus
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import ActionFlowable

_hush_pyflakes: Any
_logger: Any
encoding: str

def select_fontname(fontname, default_fontname): ...
def _open_image(filename, path: Any | None = ...): ...

class NumberedCanvas(canvas.Canvas):
    _saved_page_states: Any
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

class _rml_styles:
    localcontext: Any
    styles: Any
    styles_obj: Any
    names: Any
    table_styles: Any
    default_style: Any
    def __init__(self, nodes, localcontext) -> None: ...
    def _para_style_update(self, node): ...
    def _table_style_get(self, style_node): ...
    def para_style_get(self, node): ...

class _rml_doc:
    localcontext: Any
    etree: Any
    filename: Any
    images: Any
    path: Any
    title: Any
    def __init__(
        self,
        node,
        localcontext: Any | None = ...,
        images: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
    ) -> None: ...
    def docinit(self, els) -> None: ...
    def setTTFontMapping(self, face, fontname, filename, mode: str = ...) -> None: ...
    def _textual_image(self, node): ...
    def _images(self, el): ...
    styles: Any
    canvas: Any
    def render(self, out) -> None: ...

class _rml_canvas:
    localcontext: Any
    canvas: Any
    styles: Any
    doc_tmpl: Any
    doc: Any
    images: Any
    path: Any
    title: Any
    def __init__(
        self,
        canvas,
        localcontext,
        doc_tmpl: Any | None = ...,
        doc: Any | None = ...,
        images: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
    ) -> None: ...
    def _textual(self, node, x: int = ..., y: int = ...): ...
    def _drawString(self, node) -> None: ...
    def _drawCenteredString(self, node) -> None: ...
    def _drawRightString(self, node) -> None: ...
    def _rect(self, node) -> None: ...
    def _ellipse(self, node) -> None: ...
    def _curves(self, node) -> None: ...
    def _lines(self, node) -> None: ...
    def _grid(self, node) -> None: ...
    def _translate(self, node) -> None: ...
    def _circle(self, node) -> None: ...
    def _place(self, node) -> None: ...
    def _line_mode(self, node) -> None: ...
    def _image(self, node): ...
    def _path(self, node) -> None: ...
    def setFont(self, node): ...
    def render(self, node): ...

class _rml_draw:
    localcontext: Any
    node: Any
    styles: Any
    canvas: Any
    images: Any
    path: Any
    canvas_title: Any
    def __init__(
        self,
        localcontext,
        node,
        styles,
        images: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
    ) -> None: ...
    def render(self, canvas, doc) -> None: ...

class _rml_Illustration(platypus.flowables.Flowable):
    localcontext: Any
    node: Any
    styles: Any
    width: Any
    height: Any
    self2: Any
    def __init__(self, node, localcontext, styles, self2) -> None: ...
    def wrap(self, *args): ...
    def draw(self) -> None: ...

original_pto_split: Any

def split(self, availWidth, availHeight): ...

class _rml_flowable:
    localcontext: Any
    doc: Any
    styles: Any
    images: Any
    path: Any
    title: Any
    canvas: Any
    def __init__(
        self,
        doc,
        localcontext,
        images: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
        canvas: Any | None = ...,
    ) -> None: ...
    def _textual(self, node): ...
    def _table(self, node): ...
    def _illustration(self, node): ...
    def _textual_image(self, node): ...
    def _pto(self, node): ...
    def _flowable(self, node, extra_style: Any | None = ...): ...
    def render(self, node_story): ...

class EndFrameFlowable(ActionFlowable):
    def __init__(self, resume: int = ...) -> None: ...

class TinyDocTemplate(platypus.BaseDocTemplate):
    def beforeDocument(self) -> None: ...
    _curPageFlowableCount: int
    frame: Any
    def ___handle_pageBegin(self) -> None: ...
    page: int
    def afterPage(self) -> None: ...

class _rml_template:
    localcontext: Any
    images: Any
    path: Any
    title: Any
    doc_tmpl: Any
    page_templates: Any
    styles: Any
    doc: Any
    image: Any
    def __init__(
        self,
        localcontext,
        out,
        node,
        doc,
        images: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
    ): ...
    def render(self, node_stories) -> None: ...

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
