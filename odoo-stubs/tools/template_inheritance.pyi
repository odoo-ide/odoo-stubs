from typing import Any

_logger: Any

def add_text_before(node, text) -> None: ...
def add_text_inside(node, text) -> None: ...
def remove_element(node) -> None: ...
def locate_node(arch, spec): ...
def apply_inheritance_specs(source, specs_tree, inherit_branding: bool = ..., pre_locate=...): ...
