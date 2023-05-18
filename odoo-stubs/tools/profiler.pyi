from typing import Any, Optional

_logger: Any

class _LogTracer:
    profiles: Any
    whitelist: Any
    blacklist: Any
    files: Any
    deep: Any
    first_frame: Any
    def __init__(
        self,
        whitelist: Optional[Any] = ...,
        blacklist: Optional[Any] = ...,
        files: Optional[Any] = ...,
        deep: bool = ...,
    ) -> None: ...
    def tracer(self, frame, event, arg): ...

def profile(
    method: Optional[Any] = ...,
    whitelist: Optional[Any] = ...,
    blacklist=...,
    files: Optional[Any] = ...,
    minimum_time: int = ...,
    minimum_queries: int = ...,
): ...
