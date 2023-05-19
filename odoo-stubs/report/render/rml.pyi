from typing import Any

from . import render

class rml(render.render):
    localcontext: Any
    rml: Any
    output_type: str
    title: Any
    def __init__(
        self,
        rml,
        localcontext: Any | None = ...,
        datas: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
    ) -> None: ...

class rml2html(render.render):
    rml: Any
    localcontext: Any
    output_type: str
    def __init__(
        self, rml, localcontext: Any | None = ..., datas: Any | None = ...
    ) -> None: ...

class rml2txt(render.render):
    rml: Any
    localcontext: Any
    output_type: str
    def __init__(
        self, rml, localcontext: Any | None = ..., datas: Any | None = ...
    ) -> None: ...

class odt2odt(render.render):
    rml_dom: Any
    localcontext: Any
    output_type: str
    def __init__(
        self, rml, localcontext: Any | None = ..., datas: Any | None = ...
    ) -> None: ...

class html2html(render.render):
    rml_dom: Any
    localcontext: Any
    output_type: str
    def __init__(
        self, rml, localcontext: Any | None = ..., datas: Any | None = ...
    ) -> None: ...

class makohtml2html(render.render):
    html: Any
    localcontext: Any
    output_type: str
    def __init__(self, html, localcontext: Any | None = ...) -> None: ...
