import random
from typing import Any, Callable, Iterable, Iterator, Sequence, TypeVar

from ..tools import pycompat as pycompat

_T = TypeVar("_T")

def Random(seed) -> random.Random: ...
def format_str(val: _T, counter, values) -> _T: ...
def chain_factories(
    field_factories: Iterable[tuple[str, Callable[..., Iterator]]], model_name: str
) -> Iterator: ...
def root_factory() -> Iterator[dict]: ...
def randomize(
    vals: Sequence,
    weights: Sequence | None = ...,
    seed: Any = ...,
    formatter: Callable[[Any, Any, Any], Any] = ...,
    counter_offset: int = ...,
) -> Callable[[Iterable, str, str], dict]: ...
def cartesian(
    vals: Sequence,
    weights: Sequence | None = ...,
    seed: Any = ...,
    formatter: Callable[[Any, Any, Any], Any] = ...,
    then: Callable[[Iterable, str, str], dict] | None = ...,
) -> Callable[[Iterable, str, str], Iterator[dict]]: ...
def iterate(
    vals: Sequence,
    weights: Sequence | None = ...,
    seed: Any = ...,
    formatter: Callable[[Any, Any, Any], Any] = ...,
    then: Callable[[Iterable, str, str], dict] | None = ...,
) -> Callable[[Iterable, str, str], Iterator[dict]]: ...
def constant(
    val: Sequence, formatter: Callable[[Any, Any, Any], Any] = ...
) -> Callable[[Iterable, str, str], Iterator[dict]]: ...
def compute(
    function: Callable[[Any, Any, Any], Any], seed: Any | None = ...
) -> Callable[[Iterable, str, str], Iterator[dict]]: ...
def randint(
    a: int, b: int, seed: Any | None = ...
) -> Callable[[Iterable, str, str], Iterator[dict]]: ...
