from typing import Any, Callable

from . import server as server

_dispatchers: dict[str, Callable[[str, Any], Any]]

def dispatch_rpc(service_name: str, method: str, params): ...
