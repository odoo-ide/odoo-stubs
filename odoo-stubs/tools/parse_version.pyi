from re import Pattern
from typing import Callable, Iterator

component_re: Pattern
replace: Callable

def parse_version(s: str) -> tuple[str, ...]: ...
