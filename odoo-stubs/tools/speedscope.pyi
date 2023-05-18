from reprlib import Repr
from typing import Any, Callable, Iterable, Sequence, TypeVar

_SpeedscopeT = TypeVar("_SpeedscopeT", bound=Speedscope)

shortener: Repr
shorten: Callable[[Any], str]

class Speedscope:
    init_stack_trace: list[Sequence]
    init_stack_trace_level: int
    caller_frame: Sequence | None
    init_caller_frame: Sequence | None
    profiles_raw: dict
    name: str
    frames_indexes: dict[Any, int]
    frame_count: int
    profiles: list
    def __init__(
        self, name: str = ..., init_stack_trace: list | None = ...
    ) -> None: ...
    def add(self, key, profile) -> None: ...
    def convert_stack(self, stack: list[Sequence]) -> None: ...
    def add_output(
        self: _SpeedscopeT,
        names: Iterable[str],
        complete: bool = ...,
        display_name: str | None = ...,
        use_context: bool = ...,
        **params
    ) -> _SpeedscopeT: ...
    def add_default(self: _SpeedscopeT) -> _SpeedscopeT: ...
    def make(self) -> dict: ...
    def get_frame_id(self, frame) -> int: ...
    def stack_to_ids(
        self, stack: list, context: Iterable[tuple[int, dict]], stack_offset: int = ...
    ) -> list[int]: ...
    def process(
        self,
        entries: list[dict],
        continuous: bool = ...,
        hide_gaps: bool = ...,
        use_context: bool = ...,
        constant_time: bool = ...,
    ) -> list[dict]: ...
