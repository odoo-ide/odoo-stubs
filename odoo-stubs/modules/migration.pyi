from re import Pattern
from types import ModuleType

from ..sql_db import Cursor
from .graph import Graph, Node

VERSION_RE: Pattern

def load_script(path: str, module_name: str) -> ModuleType: ...

class MigrationManager:
    cr: Cursor
    graph: Graph
    migrations: dict
    def __init__(self, cr: Cursor, graph: Graph) -> None: ...
    def migrate_module(self, pkg: Node, stage: str) -> None: ...
