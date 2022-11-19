from typing import Any

class _LogTracer:
    profiles: dict
    whitelist: Any
    blacklist: Any
    files: Any
    deep: Any
    first_frame: Any
    def __init__(self, whitelist: Any | None = ..., blacklist: Any | None = ..., files: Any | None = ..., deep: bool = ...) -> None: ...
    def tracer(self, frame, event, arg): ...

def profile(method: Any | None = ..., whitelist: Any | None = ..., blacklist=..., files: Any | None = ..., minimum_time: int = ..., minimum_queries: int = ...): ...
