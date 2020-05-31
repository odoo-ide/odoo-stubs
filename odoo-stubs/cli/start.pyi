from . import Command as Command
from .server import main as main
from odoo.modules.module import MANIFEST_NAMES as MANIFEST_NAMES, get_module_root as get_module_root
from odoo.service.db import DatabaseExists as DatabaseExists, _create_empty_database as _create_empty_database
from typing import Any

class Start(Command):
    def get_module_list(self, path: Any): ...
    def run(self, cmdargs: Any): ...

def die(message: Any, code: int = ...) -> None: ...
