from typing import Any

from . import render
from .interface import report_int

class external_pdf(render.render):
    pdf: Any
    output_type: str
    def __init__(self, pdf) -> None: ...

class report_custom(report_int):
    def __init__(self, name) -> None: ...
    def create(self, cr, uid, ids, datas, context: Any | None = ...): ...
    obj: Any
