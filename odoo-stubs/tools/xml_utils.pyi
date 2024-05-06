from typing import Callable, Iterable, Literal

from lxml import etree
from lxml.etree import _Element
from odoo.addons.base.models.ir_attachment import IrAttachment

from ..api import Environment

def remove_control_characters(byte_node) -> str: ...

class odoo_resolver(etree.Resolver):
    env: Environment
    prefix: str | None
    def __init__(self, env: Environment, prefix: str | None) -> None: ...
    def resolve(self, url: str, id: str, context) -> str: ...

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
def load_xsd_files_from_url(
    env: Environment,
    url: str,
    file_name: str | None = ...,
    force_reload: bool = ...,
    request_max_timeout: int = ...,
    xsd_name_prefix: str = ...,
    xsd_names_filter: str | list[str] | None = ...,
    modify_xsd_content: Callable[[bytes], bytes] | None = ...,
) -> IrAttachment | Literal[False]: ...
def validate_xml_from_attachment(
    env: Environment,
    xml_content,
    xsd_name: str,
    reload_files_function: Callable | None = ...,
    prefix: str | None = ...,
) -> None: ...
def find_xml_value(xpath, xml_element: _Element, namespaces=...) -> str | None: ...
