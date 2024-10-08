from collections import OrderedDict
from typing import Generic, Iterable, Iterator, MutableMapping, TypeVar

_K = TypeVar("_K")
_V = TypeVar("_V")

class LRU(MutableMapping[_K, _V], Generic[_K, _V]):
    count: int
    d: OrderedDict
    def __init__(self, count: int, pairs: Iterable[tuple[_K, _V]] = ...) -> None: ...
    def __contains__(self, obj: _K) -> bool: ...
    def __getitem__(self, obj: _K) -> _V: ...
    def __setitem__(self, obj: _K, val: _V): ...
    def __delitem__(self, obj: _K): ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def pop(self, key: _K) -> _V: ...
    def clear(self) -> None: ...
