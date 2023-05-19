from typing import Any

class MigrationManager:
    cr: Any
    graph: Any
    migrations: Any
    def __init__(self, cr, graph) -> None: ...
    def migrate_module(self, pkg, stage): ...
