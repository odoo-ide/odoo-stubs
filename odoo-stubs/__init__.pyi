from . import api as api, fields as fields, models as models
from .modules.registry import Registry
from .tools.translate import _ as _
from typing import Any

evented: bool
multi_process: bool
SUPERUSER_ID: int

def registry(database_name: Any | None = ...) -> Registry: ...
