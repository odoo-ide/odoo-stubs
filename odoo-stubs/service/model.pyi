from typing import Any, Callable, TypeVar

from ..api import Environment
from ..sql_db import Cursor

_CallableT = TypeVar("_CallableT", bound=Callable)

PG_CONCURRENCY_ERRORS_TO_RETRY: tuple[str, str, str]
PG_CONCURRENCY_EXCEPTIONS_TO_RETRY: tuple[Exception, ...]
MAX_TRIES_ON_CONCURRENCY_FAILURE: int

def dispatch(method: str, params): ...
def execute_cr(cr: Cursor, uid: int, obj: str, method: str, *args, **kw): ...
def execute_kw(
    db: str, uid: int, obj: str, method: str, args, kw: dict | None = ...
): ...
def execute(db: str, uid: int, obj: str, method: str, *args, **kw): ...
def retrying(func: Callable[[], Any], env: Environment): ...
