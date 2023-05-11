from typing import Any

commands: Any

class CommandType(type):
    def __init__(cls, name, bases, attrs) -> None: ...

Command: Any

class Help(Command):
    def run(self, args) -> None: ...

def main() -> None: ...
