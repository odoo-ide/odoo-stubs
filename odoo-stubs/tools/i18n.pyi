from typing import Literal, Sequence

from ..api import Environment

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
