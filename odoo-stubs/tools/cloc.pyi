from typing import Any

from ..api import Environment

VERSION: int
DEFAULT_EXCLUDE: list[str]
STANDARD_MODULES: list[str]
MAX_FILE_SIZE: int
MAX_LINE_SIZE: int

class Cloc:
    modules: dict
    code: dict
    total: dict
    errors: dict
    excluded: dict
    max_width: int
    def __init__(self) -> None: ...
    def parse_xml(self, s: str) -> tuple[int, int]: ...
    def parse_py(self, s: str) -> tuple[int, int]: ...
    def parse_js(self, s: str) -> tuple[int, int]: ...
    def book(
        self,
        module: str,
        item: str = ...,
        count: tuple[Any, Any] = ...,
        exclude: bool = ...,
    ) -> None: ...
    def count_path(self, path: str, exclude: set[str] | None = ...) -> None: ...
    def count_modules(self, env: Environment) -> None: ...
    def count_customization(self, env: Environment) -> None: ...
    def count_env(self, env: Environment) -> None: ...
    def count_database(self, database) -> None: ...
    def report(self, verbose: bool = ..., width: float | None = ...): ...
