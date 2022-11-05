commands: dict[str, CommandType]

class CommandType(type):
    def __init__(cls, name, bases, attrs) -> None: ...

Command: CommandType

class Help(Command):
    def run(self, args) -> None: ...

def main() -> None: ...
