from typing import Any, Optional

safe_eval: Any

class ParseError(Exception):
    msg: Any
    text: Any
    filename: Any
    lineno: Any
    def __init__(self, msg, text, filename, lineno) -> None: ...

class RecordDictWrapper(dict):
    record: Any
    def __init__(self, record) -> None: ...
    def __getitem__(self, key): ...

def str2bool(value): ...

class xml_import:
    @staticmethod
    def nodeattr2bool(node, attr, default: bool = ...): ...
    def isnoupdate(self, data_node: Optional[Any] = ...): ...
    def get_context(self, data_node, node, eval_dict): ...
    def get_uid(self, data_node, node): ...
    def make_xml_id(self, xml_id): ...
    def id_get(self, id_str, raise_if_not_found: bool = ...): ...
    def model_id_get(self, id_str, raise_if_not_found: bool = ...): ...
    def parse(self, de, mode: Optional[Any] = ...): ...
    mode: Any
    module: Any
    env: Any
    cr: Any
    uid: Any
    idref: Any
    assertion_report: Any
    noupdate: Any
    xml_filename: Any
    def __init__(
        self,
        cr,
        module,
        idref,
        mode,
        report: Optional[Any] = ...,
        noupdate: bool = ...,
        xml_filename: Optional[Any] = ...,
    ) -> None: ...

def convert_file(
    cr,
    module,
    filename,
    idref,
    mode: str = ...,
    noupdate: bool = ...,
    kind: Optional[Any] = ...,
    report: Optional[Any] = ...,
    pathname: Optional[Any] = ...,
) -> None: ...
def convert_sql_import(cr, fp) -> None: ...
def convert_csv_import(
    cr,
    module,
    fname,
    csvcontent,
    idref: Optional[Any] = ...,
    mode: str = ...,
    noupdate: bool = ...,
) -> None: ...
def convert_xml_import(
    cr,
    module,
    xmlfile,
    idref: Optional[Any] = ...,
    mode: str = ...,
    noupdate: bool = ...,
    report: Optional[Any] = ...,
): ...
