from typing import Any, Optional

unsafe_eval = eval

def test_expr(expr, allowed_codes, mode: str = ...): ...
def const_eval(expr): ...
def safe_eval(
    expr,
    globals_dict: Optional[Any] = ...,
    locals_dict: Optional[Any] = ...,
    mode: str = ...,
    nocopy: bool = ...,
    locals_builtins: bool = ...,
): ...
