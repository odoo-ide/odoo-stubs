from typing import Any, Callable, Iterator, TypeVar

from psycopg2 import IntegrityError

from ..api import Environment
from ..exceptions import ValidationError
from ..sql_db import Cursor

PG_CONCURRENCY_ERRORS_TO_RETRY: tuple[str, str, str]
MAX_TRIES_ON_CONCURRENCY_FAILURE: int

_CallableT = TypeVar("_CallableT", bound=Callable)

def dispatch(method: str, params): ...
def execute_cr(cr: Cursor, uid: int, obj: str, method: str, *args, **kw): ...
def execute_kw(
    db: str, uid: int, obj: str, method: str, args, kw: dict | None = ...
): ...
def execute(db: str, uid: int, obj: str, method: str, *args, **kw): ...
def _as_validation_error(env: Environment, exc: IntegrityError) -> ValidationError: ...
def retrying(func: Callable[[], Any], env: Environment): ...
def _traverse_containers(val, type_) -> Iterator: ...
