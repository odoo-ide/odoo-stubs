from typing import Any

LOG_NOTSET: str
LOG_DEBUG: str
LOG_INFO: str
LOG_WARNING: str
LOG_ERROR: str
LOG_CRITICAL: str

def get_encodings(hint_encoding: str = ...) -> None: ...

text_type: Any

def ustr(value, hint_encoding: str = ..., errors: str = ...): ...
def exception_to_unicode(e): ...
