from typing import Any

_logger: Any

class MigrationManager:
    cr: Any
    graph: Any
    migrations: Any
    def __init__(self, cr, graph) -> None: ...
    def _get_files(self): ...
    def migrate_module(self, pkg, stage): ...
