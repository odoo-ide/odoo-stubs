from typing import Any

commands: Any

class CommandType(type):
    def __init__(cls, name: Any, bases: Any, attrs: Any) -> None: ...

Command: Any

class Help(Command):
    def run(self, args: Any) -> None: ...

def main() -> None: ...
