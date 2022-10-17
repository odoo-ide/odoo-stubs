from ..tools.config import configmanager

SUPPORTED_DEBUGGER: set[str]

def post_mortem(config: configmanager, info) -> None: ...
