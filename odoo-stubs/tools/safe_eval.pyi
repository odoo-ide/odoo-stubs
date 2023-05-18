from typing import Any

unsafe_eval = eval
__all__: Any
_ALLOWED_MODULES: Any
_UNSAFE_ATTRIBUTES: Any
_CONST_OPCODES: Any
_EXPR_OPCODES: Any
_SAFE_OPCODES: Any
_logger: Any

def _get_opcodes(codeobj) -> None: ...
def assert_no_dunder_name(code_obj, expr) -> None: ...
def assert_valid_codeobj(allowed_codes, code_obj, expr) -> None: ...
def test_expr(expr, allowed_codes, mode: str = ...): ...
def const_eval(expr): ...
def expr_eval(expr): ...
def _import(
    name,
    globals: Any | None = ...,
    locals: Any | None = ...,
    fromlist: Any | None = ...,
    level: int = ...,
): ...

_BUILTINS: Any

def safe_eval(
    expr,
    globals_dict: Any | None = ...,
    locals_dict: Any | None = ...,
    mode: str = ...,
    nocopy: bool = ...,
    locals_builtins: bool = ...,
): ...
def test_python_expr(expr, mode: str = ...): ...
