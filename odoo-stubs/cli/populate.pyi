from . import Command
from typing import Any

_logger: Any

class Populate(Command):
    def run(self, cmdargs) -> None: ...
    @classmethod
    def populate(cls, env, size, model_patterns: bool = ...): ...
    @classmethod
    def _get_ordered_models(cls, env, model_patterns: bool = ...): ...
