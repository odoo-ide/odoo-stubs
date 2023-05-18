from types import ModuleType

from ..sql_db import Cursor
from .graph import Graph, Node

def load_script(path: str, module_name: str) -> ModuleType: ...

class MigrationManager:
    cr: Cursor
    graph: Graph
    migrations: dict
    def __init__(self, cr: Cursor, graph: Graph) -> None: ...
    def _get_files(self) -> None: ...
    def migrate_module(self, pkg: Node, stage: str) -> None: ...
