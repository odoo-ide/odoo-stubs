from types import CodeType
from typing import Any, Iterator, Literal

from opcode import HAVE_ARGUMENT as HAVE_ARGUMENT

unsafe_eval = eval
_ALLOWED_MODULES: list[str]
_UNSAFE_ATTRIBUTES: list[str]
_POSSIBLE_OPCODES_P3: list[str]
_CONST_OPCODES: set[int]
_EXPR_OPCODES: set[int]
_SAFE_OPCODES: set[int]

def _get_opcodes(codeobj) -> Iterator[int]: ...
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
