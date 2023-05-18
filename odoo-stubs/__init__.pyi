from typing import Any

from . import api as api
from . import fields as fields
from . import models as models
from .modules.registry import Registry
from .tools.translate import _ as _

evented: bool
multi_process: bool
SUPERUSER_ID: int

def registry(database_name: Any | None = ...) -> Registry: ...
