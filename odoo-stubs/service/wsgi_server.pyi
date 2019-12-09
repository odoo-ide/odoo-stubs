# Stubs for odoo.service.wsgi_server (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

RPC_FAULT_CODE_CLIENT_ERROR: int
RPC_FAULT_CODE_APPLICATION_ERROR: int
RPC_FAULT_CODE_WARNING: int
RPC_FAULT_CODE_ACCESS_DENIED: int
RPC_FAULT_CODE_ACCESS_ERROR: int

def xmlrpc_handle_exception_int(e: Any): ...
def xmlrpc_handle_exception_string(e: Any): ...
def application_unproxied(environ: Any, start_response: Any): ...
def application(environ: Any, start_response: Any): ...
