from re import Pattern

class UserAgentParser(object):
    platforms: list[tuple[str, Pattern]]
    browsers: list[tuple[str, Pattern]]
    _browser_version_re: str
    _language_re: Pattern
    def __init__(self) -> None: ...
    def __call__(
        self, user_agent: str
    ) -> tuple[str | None, str | None, str | None, str | None]: ...

class UserAgent(object):
    _parser: UserAgentParser
    string: str
    platform: str | None
    browser: str | None
    version: str | None
    language: str | None
    def __init__(self, environ_or_string: dict | str): ...
    def to_header(self) -> str: ...
    def __str__(self) -> str: ...
    def __nonzero__(self) -> bool: ...
    __bool__ = __nonzero__
    def __repr__(self) -> str: ...
