from typing import Any

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
    def isnoupdate(self, data_node: Any | None = ...): ...
    def get_context(self, data_node, node, eval_dict): ...
    def get_uid(self, data_node, node): ...
    def id_get(self, id_str, raise_if_not_found: bool = ...): ...
    def model_id_get(self, id_str, raise_if_not_found: bool = ...): ...
    def parse(self, de, mode: Any | None = ...): ...
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
        report: Any | None = ...,
        noupdate: bool = ...,
        xml_filename: Any | None = ...,
    ) -> None: ...

def convert_file(
    cr,
    module,
    filename,
    idref,
    mode: str = ...,
    noupdate: bool = ...,
    kind: Any | None = ...,
    report: Any | None = ...,
    pathname: Any | None = ...,
) -> None: ...
def convert_sql_import(cr, fp) -> None: ...
def convert_csv_import(
    cr,
    module,
    fname,
    csvcontent,
    idref: Any | None = ...,
    mode: str = ...,
    noupdate: bool = ...,
) -> None: ...
def convert_xml_import(
    cr,
    module,
    xmlfile,
    idref: Any | None = ...,
    mode: str = ...,
    noupdate: bool = ...,
    report: Any | None = ...,
): ...
