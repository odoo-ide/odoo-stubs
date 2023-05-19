from typing import Any

from ..interface import report_int

class report_printscreen_list(report_int):
    context: Any
    groupby: Any
    cr: str
    def __init__(self, name) -> None: ...
    groupby_no_leaf: Any
    title: Any
    def create(self, cr, uid, ids, datas, context: Any | None = ...): ...
    obj: Any
