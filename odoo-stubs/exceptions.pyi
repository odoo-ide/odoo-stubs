from typing import Any

class except_orm(Exception):
    name: Any
    value: Any
    args: Any
    def __init__(self, name, value: Any | None = ...) -> None: ...

class UserError(except_orm):
    def __init__(self, msg) -> None: ...

Warning = UserError

class RedirectWarning(Exception):
    @property
    def name(self): ...

class AccessDenied(Exception):
    traceback: Any
    def __init__(self) -> None: ...

class AccessError(except_orm):
    def __init__(self, msg) -> None: ...

class MissingError(except_orm):
    def __init__(self, msg) -> None: ...

class ValidationError(except_orm):
    def __init__(self, msg) -> None: ...

class DeferredException(Exception):
    message: Any
    traceback: Any
    def __init__(self, msg, tb) -> None: ...

class QWebException(Exception): ...
