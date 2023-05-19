import logging.handlers
from typing import Any, Optional

def log(logger, level, prefix, msg, depth: Optional[Any] = ...) -> None: ...

class PostgreSQLHandler(logging.Handler):
    def emit(self, record) -> None: ...

BLACK: Any
RED: Any
GREEN: Any
YELLOW: Any
BLUE: Any
MAGENTA: Any
CYAN: Any
WHITE: Any
_NOTHING: Any
DEFAULT: Any
RESET_SEQ: str
COLOR_SEQ: str
BOLD_SEQ: str
COLOR_PATTERN: Any
LEVEL_COLOR_MAPPING: Any

class DBFormatter(logging.Formatter):
    def format(self, record): ...

class ColoredFormatter(DBFormatter):
    def format(self, record): ...

def init_logger(): ...

DEFAULT_LOG_CONFIGURATION: Any
PSEUDOCONFIG_MAPPER: Any
