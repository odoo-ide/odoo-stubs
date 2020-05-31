from . import Command
from typing import Any

_logger: Any

class Populate(Command):
    def run(self, cmdargs: Any) -> None: ...
    @classmethod
    def populate(cls, env: Any, size: Any, model_patterns: bool = ...): ...
    @classmethod
    def _get_ordered_models(cls, env: Any, model_patterns: bool = ...): ...
