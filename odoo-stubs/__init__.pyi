from . import addons as addons, api as api, cli as cli, conf as conf, fields as fields, http as http, loglevels as loglevels, models as models, netsvc as netsvc, osv as osv, release as release, service as service, sql_db as sql_db, tools as tools, upgrade as upgrade
from odoo.tools.translate import _ as _, _lt as _lt
from typing import Any, Optional

__path__: Any
evented: bool

def gevent_wait_callback(conn: Any, timeout: Optional[Any] = ...) -> None: ...

multi_process: bool

def _decompress(data: Any): ...

SUPERUSER_ID: int

def registry(database_name: Optional[Any] = ...): ...
