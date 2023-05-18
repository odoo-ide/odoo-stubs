from re import Pattern
from typing import Any, Iterable

from markupsafe import Markup

INLINE_TEMPLATE_REGEX: Pattern

def relativedelta_proxy(*args, **kwargs): ...

template_env_globals: dict[str, Any]

def parse_inline_template(text: str) -> list[tuple[str, str]]: ...
def convert_inline_template_to_qweb(template: str) -> Markup: ...
def render_inline_template(
    template_instructions: Iterable[tuple[str, str]], variables: dict
) -> str: ...
