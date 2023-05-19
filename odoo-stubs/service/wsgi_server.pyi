from typing import Callable

from werkzeug.middleware.proxy_fix import ProxyFix as ProxyFix_

RPC_FAULT_CODE_CLIENT_ERROR: int
RPC_FAULT_CODE_APPLICATION_ERROR: int
RPC_FAULT_CODE_WARNING: int
RPC_FAULT_CODE_ACCESS_DENIED: int
RPC_FAULT_CODE_ACCESS_ERROR: int

def xmlrpc_handle_exception_int(e: Exception) -> str: ...
def xmlrpc_handle_exception_string(e: Exception) -> str: ...
def application_unproxied(environ, start_response): ...

ProxyFix: Callable[..., ProxyFix_]

def application(environ, start_response): ...
