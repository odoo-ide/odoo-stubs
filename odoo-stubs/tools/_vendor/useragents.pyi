from re import Pattern

class UserAgentParser(object):
    platforms: list[tuple[str, Pattern]]
    browsers: list[tuple[str, Pattern]]
    def __init__(self) -> None: ...
    def __call__(
        self, user_agent: str
    ) -> tuple[str | None, str | None, str | None, str | None]: ...

class UserAgent(object):
    string: str
    platform: str | None
    browser: str | None
    version: str | None
    language: str | None
    def __init__(self, environ_or_string: dict | str): ...
    def to_header(self) -> str: ...
    def __nonzero__(self) -> bool: ...
    __bool__ = __nonzero__
