from collections import defaultdict
from typing import Any, Callable, TypeVar

from ..models import BaseModel
from .lru import LRU

_CallableT = TypeVar("_CallableT")

unsafe_eval = eval

class ormcache_counter:
    hit: int
    miss: int
    err: int
    def __init__(self) -> None: ...
    @property
    def ratio(self) -> float: ...

STAT: defaultdict[Any, ormcache_counter]

class ormcache:
    args: Any
    skiparg: Any
    cache_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    method: Callable
    def __call__(self, method: _CallableT) -> _CallableT: ...
    def add_value(self, *args, cache_value: Any | None = ..., **kwargs) -> None: ...
    key: Any
    def determine_key(self): ...
    def lru(
        self, model: BaseModel
    ) -> tuple[LRU, tuple[str, Callable], ormcache_counter]: ...
    def lookup(self, method: Callable, *args, **kwargs): ...
    def clear(self, model: BaseModel, *args) -> None: ...

class ormcache_context(ormcache):
    keys: Any
    def __init__(self, *args, **kwargs) -> None: ...
    key: Any
    def determine_key(self) -> None: ...

def log_ormcache_stats(sig: Any | None = ..., frame: Any | None = ...): ...
def get_cache_key_counter(bound_method, *args, **kwargs): ...

cache = ormcache
