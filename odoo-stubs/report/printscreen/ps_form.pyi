from typing import Any

from ..interface import report_int

class report_printscreen_list(report_int):
    title: Any
    def create(self, cr, uid, ids, datas, context: Any | None = ...): ...
    obj: Any
