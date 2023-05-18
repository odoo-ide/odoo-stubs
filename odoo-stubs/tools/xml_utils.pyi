from typing import IO, Iterable

from lxml import etree
from lxml.etree import _Element

from ..api import Environment

class odoo_resolver(etree.Resolver):
    env: Environment
    def __init__(self, env: Environment) -> None: ...
    def resolve(self, url: str, id: str, context) -> str: ...

def _check_with_xsd(
    tree_or_str: str | _Element, stream: str | IO, env: Environment | None = ...
) -> None: ...
def create_xml_node_chain(
    first_parent_node: _Element,
    nodes_list: Iterable[str],
    last_node_value: str | None = ...,
) -> list[_Element]: ...
def create_xml_node(
    parent_node: _Element, node_name: str, node_value: str | None = ...
) -> _Element: ...
def cleanup_xml_node(
    xml_node_or_string: _Element | str,
    remove_blank_text: bool = ...,
    remove_blank_nodes: bool = ...,
    indent_level: int = ...,
    indent_space: str = ...,
) -> _Element: ...
