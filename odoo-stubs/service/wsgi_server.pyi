from typing import Any

_logger: Any
RPC_FAULT_CODE_CLIENT_ERROR: int
RPC_FAULT_CODE_APPLICATION_ERROR: int
RPC_FAULT_CODE_WARNING: int
RPC_FAULT_CODE_ACCESS_DENIED: int
RPC_FAULT_CODE_ACCESS_ERROR: int

def xmlrpc_handle_exception_int(e): ...
def xmlrpc_handle_exception_string(e): ...
def application_unproxied(environ, start_response): ...

ProxyFix: Any

def application(environ, start_response): ...
