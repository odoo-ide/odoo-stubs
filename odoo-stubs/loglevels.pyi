from typing import Generator

LOG_NOTSET: str
LOG_DEBUG: str
LOG_INFO: str
LOG_WARNING: str
LOG_ERROR: str
LOG_CRITICAL: str

def get_encodings(hint_encoding: str = ...) -> Generator[str, None, None]: ...

text_type: type[str]

def ustr(value, hint_encoding: str = ..., errors: str = ...) -> str: ...
def exception_to_unicode(e: BaseException) -> str: ...
