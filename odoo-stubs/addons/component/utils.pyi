from .core import ComponentRegistry

def get_component_registry(dbname: str) -> ComponentRegistry: ...
def is_component_registry_ready(dbname: str) -> bool: ...