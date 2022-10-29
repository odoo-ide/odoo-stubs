from psycopg2 import connection

from . import (
    addons as addons,
    api as api,
    cli as cli,
    conf as conf,
    fields as fields,
    http as http,
    loglevels as loglevels,
    models as models,
    netsvc as netsvc,
    osv as osv,
    release as release,
    service as service,
    sql_db as sql_db,
    tools as tools,
    upgrade as upgrade
)
from .api import Registry
from .tools.translate import _ as _, _lt as _lt

evented: bool

def gevent_wait_callback(conn: connection, timeout: float | None = ...) -> None: ...

multi_process: bool

def _decompress(data: bytes) -> bytes: ...

SUPERUSER_ID: int

def registry(database_name: str | None = ...) -> Registry: ...
