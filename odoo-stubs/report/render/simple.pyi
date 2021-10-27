from . import render
from typing import Any

class simple(render.render):
    result: Any
    def _render(self): ...
