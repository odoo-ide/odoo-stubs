from types import CodeType
from typing import Literal

from opcode import HAVE_ARGUMENT as HAVE_ARGUMENT

unsafe_eval = eval

def assert_no_dunder_name(code_obj: CodeType, expr: str) -> None: ...
def assert_valid_codeobj(
    allowed_codes: set[int], code_obj: CodeType, expr: str
) -> None: ...
def test_expr(expr: str, allowed_codes: set[int], mode: str = ...): ...
def const_eval(expr: str): ...
def expr_eval(expr: str): ...
def safe_eval(
    expr: str,
    globals_dict: dict | None = ...,
    locals_dict: dict | None = ...,
    mode: str = ...,
    nocopy: bool = ...,
    locals_builtins: bool = ...,
): ...
def test_python_expr(expr: str, mode: str = ...) -> str | Literal[False]: ...
