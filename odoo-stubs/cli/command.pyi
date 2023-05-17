commands: dict[str, type[Command]]

class Command:
    name: str
    def __init_subclass__(cls) -> None: ...

ODOO_HELP: str

class Help(Command):
    def run(self, args) -> None: ...

def main() -> None: ...
