from typing import Any, Optional

from . import addons as addons
from . import api as api
from . import conf as conf
from . import fields as fields
from . import http as http
from . import loglevels as loglevels
from . import models as models
from . import netsvc as netsvc
from . import osv as osv
from . import release as release
from . import service as service
from . import sql_db as sql_db
from . import tools as tools
from .tools.translate import _ as _

__path__: Any
evented: bool

def gevent_wait_callback(conn, timeout: Optional[Any] = ...) -> None: ...

multi_process: bool
_babelCoreParseLocale: Any

def _babelCoreParseLocale_unitag(identifier, sep: str = ...): ...
def _decompress(data): ...

SUPERUSER_ID: int

def registry(database_name: Optional[Any] = ...): ...
