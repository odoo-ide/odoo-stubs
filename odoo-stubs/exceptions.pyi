from .fields import Field
from .models import BaseModel

class UserError(Exception):
    def __init__(self, message: str) -> None: ...

class RedirectWarning(Exception):
    def __init__(
        self,
        message: str,
        action: int,
        button_text: str,
        additional_context: dict | None = ...,
    ) -> None: ...
    @property
    def name(self): ...

class AccessDenied(UserError):
    traceback: tuple[str, str, str]
    def __init__(self, message: str = ...) -> None: ...

class AccessError(UserError): ...

class CacheMiss(KeyError):
    def __init__(self, record: BaseModel, field: Field) -> None: ...

class MissingError(UserError): ...
class ValidationError(UserError): ...
