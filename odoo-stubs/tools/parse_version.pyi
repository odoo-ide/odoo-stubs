from re import Pattern
from typing import Callable

component_re: Pattern
replace: Callable

def parse_version(s: str) -> tuple[str]: ...
