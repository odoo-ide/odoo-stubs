from re import Pattern
from typing import Callable, Iterator

component_re: Pattern
replace: Callable

def _parse_version_parts(s: str) -> Iterator[str]: ...
def parse_version(s: str) -> tuple[str]: ...
