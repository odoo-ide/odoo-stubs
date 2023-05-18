from types import CodeType
from typing import Any, Iterable, Iterator, Literal

from opcode import HAVE_ARGUMENT as HAVE_ARGUMENT

unsafe_eval = eval
_ALLOWED_MODULES: list[str]
_UNSAFE_ATTRIBUTES: list[str]

def to_opcodes(
    opnames: Iterable[str], _opmap: dict[str, int] = ...
) -> Iterator[int]: ...

_BLACKLIST: set[int]
_CONST_OPCODES: set[int]
_operations: list[str]
_EXPR_OPCODES: set[int]
_SAFE_OPCODES: set[int]

def assert_no_dunder_name(code_obj: CodeType, expr: str) -> None: ...
def assert_valid_codeobj(
    allowed_codes: set[int], code_obj: CodeType, expr: str
) -> None: ...
def test_expr(expr: str, allowed_codes: set[int], mode: str = ...): ...
def const_eval(expr: str): ...
def expr_eval(expr: str): ...
def _import(
    name: str,
    globals: dict | None = ...,
    locals: dict | None = ...,
    fromlist: list | None = ...,
    level: int = ...,
): ...

_BUILTINS: dict[str, Any]

def safe_eval(
    expr: str,
    globals_dict: dict | None = ...,
    locals_dict: dict | None = ...,
    mode: str = ...,
    nocopy: bool = ...,
    locals_builtins: bool = ...,
): ...
def test_python_expr(expr: str, mode: str = ...) -> str | Literal[False]: ...
def check_values(d: dict): ...

class wrap_module:
    _repr: str
    def __init__(self, module, attributes) -> None: ...
    def __repr__(self) -> str: ...
    def __getattr__(self, item): ...

mods: list[str]
datetime: wrap_module
json: wrap_module
time: wrap_module
pytz: wrap_module
