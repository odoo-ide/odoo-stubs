from typing import Any

_logger: Any
_test_logger: Any

def load_module_graph(
    cr,
    graph,
    status: Any | None = ...,
    perform_checks: bool = ...,
    skip_modules: Any | None = ...,
    report: Any | None = ...,
    models_to_check: Any | None = ...,
): ...
def _check_module_names(cr, module_names) -> None: ...
def load_marked_modules(
    cr,
    graph,
    states,
    force,
    progressdict,
    report,
    loaded_modules,
    perform_checks,
    models_to_check: Any | None = ...,
): ...
def load_modules(
    db, force_demo: bool = ..., status: Any | None = ..., update_module: bool = ...
): ...
def reset_modules_state(db_name) -> None: ...
