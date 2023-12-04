import csv
from collections import defaultdict, namedtuple
from re import Pattern
from tarfile import TarFile
from typing import IO, Any, BinaryIO, Callable, Iterable, Iterator, NoReturn

from lxml.etree import _Element
from polib import POFile

from ..api import Environment
from ..sql_db import Cursor
from .pycompat import _CsvWriter

PYTHON_TRANSLATION_COMMENT: str
JAVASCRIPT_TRANSLATION_COMMENT: str
SKIPPED_ELEMENTS: tuple[str, ...]

class UNIX_LINE_TERMINATOR(csv.excel):
    lineterminator: str

def encode(s: str) -> str: ...

TRANSLATED_ELEMENTS: set[str]
TRANSLATED_ATTRS: dict[str, Any]

def translate_attrib_value(node: _Element) -> bool: ...

avoid_pattern: Pattern

def translate_xml_node(
    node: _Element,
    callback: Callable[[str], str | None],
    parse: Callable[[str], _Element],
    serialize: Callable[[_Element], str],
) -> _Element: ...
def parse_xml(text: str) -> _Element: ...
def serialize_xml(node: _Element) -> str: ...
def parse_html(text: str) -> _Element: ...
def serialize_html(node: _Element) -> str: ...
def xml_translate(callback: Callable[[str], str | None], value: str) -> str: ...
def xml_term_converter(value: str) -> str: ...
def html_translate(callback: Callable[[str], str | None], value: str) -> str: ...
def html_term_converter(value: str) -> str: ...
def get_text_content(term: str) -> str: ...
def translate_sql_constraint(cr: Cursor, key: str, lang: str) -> str: ...

class GettextAlias:
    def __call__(self, source: str, *args, **kwargs) -> str: ...

class _lt:
    def __init__(self, source: str, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> NoReturn: ...
    def __lt__(self, other) -> NoReturn: ...
    def __add__(self, other: str | _lt) -> str: ...
    def __radd__(self, other: str) -> str: ...

_: GettextAlias

def quote(s: str) -> str: ...

re_escaped_char: Pattern
re_escaped_replacements: dict[str, str]

def unquote(str: str) -> str: ...
def TranslationFileReader(
    source: IO, fileformat: str = ...
) -> CSVFileReader | PoFileReader: ...

class CSVFileReader:
    source: csv.DictReader
    prev_code_src: str
    def __init__(self, source: IO) -> None: ...
    def __iter__(self) -> Iterator[csv.DictReader]: ...

class PoFileReader:
    pofile: POFile
    def __init__(self, source: str | IO): ...
    def __iter__(self) -> Iterator[dict[str, Any]]: ...

def TranslationFileWriter(
    target, fileformat: str = ..., lang: str | None = ...
) -> CSVFileWriter | PoFileWriter | TarFileWriter: ...

class CSVFileWriter:
    writer: _CsvWriter
    def __init__(self, target: BinaryIO) -> None: ...
    def write_rows(self, rows: Iterable) -> None: ...

class PoFileWriter:
    buffer: IO
    lang: str
    po: POFile
    def __init__(self, target: IO, lang: str) -> None: ...
    def write_rows(self, rows: Iterable) -> None: ...
    def add_entry(
        self, modules, tnrs, source, trad, comments: Iterable[str] | None = ...
    ) -> None: ...

class TarFileWriter:
    tar: TarFile
    lang: str
    def __init__(self, target: IO, lang: str) -> None: ...
    def write_rows(self, rows: Iterable) -> None: ...

def trans_export(
    lang: str, modules: list[str], buffer, format: str, cr: Cursor
) -> None: ...
def trans_export_records(
    lang: str, model_name: str, ids, buffer, format: str, cr: Cursor
) -> None: ...
def babel_extract_qweb(fileobj: IO, keywords, comment_tags, options) -> list[tuple]: ...
def extract_formula_terms(formula: str) -> Iterator[str]: ...
def extract_spreadsheet_terms(
    fileobj, keywords, comment_tags, options
) -> Iterator[tuple[int, str, str, list]]: ...

ImdInfo = namedtuple("ExternalId", ["name", "model", "res_id", "module"])

class TranslationReader:
    env: Environment
    def __init__(self, cr: Cursor, lang: str | None = ...) -> None: ...
    def __iter__(self) -> Iterable[tuple]: ...

class TranslationRecordReader(TranslationReader): ...
class TranslationModuleReader(TranslationReader): ...

def DeepDefaultDict() -> defaultdict: ...

class TranslationImporter:
    cr: Cursor
    verbose: bool
    env: Environment
    model_translations: defaultdict[
        str, defaultdict[str, defaultdict[str, defaultdict]]
    ]
    model_terms_translations: defaultdict[
        str, defaultdict[str, defaultdict[str, defaultdict]]
    ]
    def __init__(self, cr: Cursor, verbose: bool = ...) -> None: ...
    def load_file(
        self, filepath: str, lang: str, xmlids: Iterable[str] | None = ...
    ) -> None: ...
    def load(
        self,
        fileobj: IO,
        fileformat: str,
        lang: str,
        xmlids: Iterable[str] | None = ...,
    ) -> None: ...
    def save(self, overwrite: bool = ..., force_overwrite: bool = ...) -> None: ...

def trans_load(
    cr: Cursor, filepath: str, lang: str, verbose: bool = ..., overwrite: bool = ...
) -> None: ...
def trans_load_data(
    cr: Cursor,
    fileobj: IO,
    fileformat: str,
    lang: str,
    verbose: bool = ...,
    overwrite: bool = ...,
) -> None: ...
def get_locales(lang: str | None = ...) -> None: ...
def resetlocale() -> str: ...
def load_language(cr: Cursor, lang: str) -> None: ...
def get_po_paths(module_name: str, lang: str) -> list[str]: ...

class CodeTranslations:
    python_translations: dict[tuple[str, str], dict]
    web_translations: dict[tuple[str, str], dict]
    def __init__(self) -> None: ...
    def get_python_translations(self, module_name: str, lang: str) -> dict: ...
    def get_web_translations(self, module_name: str, lang: str) -> dict: ...

code_translations: CodeTranslations
