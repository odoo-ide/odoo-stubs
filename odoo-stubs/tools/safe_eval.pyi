from typing import Any, Optional

unsafe_eval = eval
__all__: Any
_ALLOWED_MODULES: Any
_UNSAFE_ATTRIBUTES: Any
_POSSIBLE_OPCODES_P3: Any
_CONST_OPCODES: Any
_EXPR_OPCODES: Any
_SAFE_OPCODES: Any
_logger: Any

def _get_opcodes(codeobj): ...
def assert_no_dunder_name(code_obj, expr) -> None: ...
def assert_valid_codeobj(allowed_codes, code_obj, expr) -> None: ...
def test_expr(expr, allowed_codes, mode: str = ...): ...
def const_eval(expr): ...
def expr_eval(expr): ...
def _import(
    name,
    globals: Optional[Any] = ...,
    locals: Optional[Any] = ...,
    fromlist: Optional[Any] = ...,
    level: int = ...,
): ...

_BUILTINS: Any

def safe_eval(
    expr,
    globals_dict: Optional[Any] = ...,
    locals_dict: Optional[Any] = ...,
    mode: str = ...,
    nocopy: bool = ...,
    locals_builtins: bool = ...,
): ...
def test_python_expr(expr, mode: str = ...): ...
