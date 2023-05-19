from typing import Any

from ..api import Environment
from ..tests.result import OdooTestResult
from .graph import Graph, Node
from .registry import Registry

def load_data(
    env: Environment, idref: dict, mode: str, kind: str, package: Node
) -> bool: ...
def load_demo(env: Environment, package: Node, idref: dict, mode: str) -> bool: ...
def force_demo(env: Environment) -> None: ...
def load_module_graph(
    env: Environment,
    graph: Graph,
    status: Any | None = ...,
    perform_checks: Any = ...,
    skip_modules: list[str] | None = ...,
    report: OdooTestResult | None = ...,
    models_to_check: set[str] | None = ...,
) -> tuple[list[str], list[str]]: ...
def load_marked_modules(
    env: Environment,
    graph: Graph,
    states: list[str],
    force: list[str],
    progressdict,
    report: OdooTestResult,
    loaded_modules: list[str],
    perform_checks: Any,
    models_to_check: set[str] | None = ...,
) -> list[str]: ...
def load_modules(
    registry: Registry,
    force_demo: bool = ...,
    status: Any | None = ...,
    update_module: Any = ...,
) -> Registry | None: ...
def reset_modules_state(db_name: str) -> None: ...
