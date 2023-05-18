from psycopg2 import connection

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
from .api import Registry
from .fields import Command as Command
from .tools.translate import _ as _
from .tools.translate import _lt as _lt

evented: bool

def gevent_wait_callback(conn: connection, timeout: float | None = ...) -> None: ...

multi_process: bool

def _decompress(data: bytes) -> bytes: ...

SUPERUSER_ID: int

def registry(database_name: str | None = ...) -> Registry: ...
