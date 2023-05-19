from io import BufferedReader
from typing import Any, Callable, TextIO

from lxml.etree import _Element

from ..api import Environment
from ..sql_db import Cursor
from .misc import ustr as ustr

safe_eval: Callable

class ParseError(Exception): ...

class RecordDictWrapper(dict):
    record: Any
    def __init__(self, record) -> None: ...
    def __getitem__(self, key): ...

def str2bool(value) -> bool: ...
def nodeattr2bool(node: _Element, attr, default: bool = ...) -> bool: ...

class xml_import:
    def get_env(
        self, node: _Element, eval_context: dict | None = ...
    ) -> Environment: ...
    def make_xml_id(self, xml_id: str) -> str: ...
    def id_get(self, id_str: str, raise_if_not_found: bool = ...) -> int | None: ...
    def model_id_get(
        self, id_str: str, raise_if_not_found: bool = ...
    ) -> tuple[Any, Any]: ...
    @property
    def env(self) -> Environment: ...
    @property
    def noupdate(self) -> bool: ...
    mode: str
    module: str
    envs: list[Environment]
    idref: dict
    xml_filename: str
    def __init__(
        self,
        cr: Cursor,
        module: str,
        idref: dict,
        mode: str,
        noupdate: bool = ...,
        xml_filename: str | None = ...,
    ) -> None: ...
    def parse(self, de: _Element) -> None: ...
    DATA_ROOTS: list[str]

def convert_file(
    cr: Cursor,
    module: str,
    filename: str,
    idref: dict,
    mode: str = ...,
    noupdate: bool = ...,
    kind: str | None = ...,
    pathname: str | None = ...,
) -> None: ...
def convert_sql_import(cr: Cursor, fp: TextIO) -> None: ...
def convert_csv_import(
    cr: Cursor,
    module: str,
    fname: str,
    csvcontent: bytes,
    idref: dict | None = ...,
    mode: str = ...,
    noupdate: bool = ...,
) -> None: ...
def convert_xml_import(
    cr: Cursor,
    module: str,
    xmlfile: str | BufferedReader,
    idref: dict | None = ...,
    mode: str = ...,
    noupdate: bool = ...,
    report: Any | None = ...,
) -> None: ...
