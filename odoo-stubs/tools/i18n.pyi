from re import Pattern
from typing import Literal, Sequence

from ..api import Environment

XPG_LOCALE_RE: Pattern

def format_list(
    env: Environment,
    lst: Sequence[str],
    style: Literal[
        "standard",
        "standard-short",
        "or",
        "or-short",
        "unit",
        "unit-short",
        "unit-narrow",
    ] = ...,
    lang_code: str | None = ...,
) -> str: ...
def py_to_js_locale(locale: str) -> str: ...
