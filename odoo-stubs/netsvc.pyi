import logging.handlers
from typing import Any, Optional

_logger: Any

def log(logger: Any, level: Any, prefix: Any, msg: Any, depth: Optional[Any] = ...) -> None: ...

class PostgreSQLHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...

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

class PerfFilter(logging.Filter):
    def format_perf(self, query_count: Any, query_time: Any, remaining_time: Any): ...
    def filter(self, record: Any): ...

class ColoredPerfFilter(PerfFilter):
    def format_perf(self, query_count: Any, query_time: Any, remaining_time: Any): ...

class DBFormatter(logging.Formatter):
    def format(self, record: Any): ...

class ColoredFormatter(DBFormatter):
    def format(self, record: Any): ...

_logger_init: bool

def init_logger(): ...

DEFAULT_LOG_CONFIGURATION: Any
PSEUDOCONFIG_MAPPER: Any
