from typing import Any, Optional

def load_module_graph(
    cr,
    graph,
    status: Optional[Any] = ...,
    perform_checks: bool = ...,
    skip_modules: Optional[Any] = ...,
    report: Optional[Any] = ...,
    models_to_check: Optional[Any] = ...,
): ...
def load_marked_modules(
    cr,
    graph,
    states,
    force,
    progressdict,
    report,
    loaded_modules,
    perform_checks,
    models_to_check: Optional[Any] = ...,
): ...
def load_modules(
    db, force_demo: bool = ..., status: Optional[Any] = ..., update_module: bool = ...
): ...
def reset_modules_state(db_name) -> None: ...
