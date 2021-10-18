import logging.handlers
from typing import Any

_logger: Any

def log(logger, level, prefix, msg, depth: Any | None = ...) -> None: ...

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

class PerfFilter(logging.Filter):
    def format_perf(self, query_count, query_time, remaining_time): ...
    def filter(self, record): ...

class ColoredPerfFilter(PerfFilter):
    def format_perf(self, query_count, query_time, remaining_time): ...

class DBFormatter(logging.Formatter):
    def format(self, record): ...

class ColoredFormatter(DBFormatter):
    def format(self, record): ...

_logger_init: bool

def init_logger(): ...

DEFAULT_LOG_CONFIGURATION: Any
PSEUDOCONFIG_MAPPER: Any
showwarning: Any
IGNORE: Any

def showwarning_with_traceback(message, category, filename, lineno, file: Any | None = ..., line: Any | None = ...): ...
def runbot(self, message, *args, **kws) -> None: ...
