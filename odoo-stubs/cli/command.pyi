from typing import Any

commands: Any

class CommandType(type):
    def __init__(cls, name, bases, attrs) -> None: ...

class Command:
    __metaclass__: Any
    def run(self, args) -> None: ...

class Help(Command):
    def run(self, args) -> None: ...

def main() -> None: ...
