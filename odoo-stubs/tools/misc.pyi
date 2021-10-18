from .cache import *
import pickle as pickle_
import xlsxwriter
import xlwt
from .parse_version import parse_version as parse_version
from collections.abc import Mapping, MutableMapping, MutableSet
from odoo.loglevels import exception_to_unicode as exception_to_unicode, get_encodings as get_encodings
from typing import Any

_logger: Any
SKIPPED_ELEMENT_TYPES: Any

def find_in_path(name): ...
def _exec_pipe(prog, args, env: Any | None = ...): ...
def exec_command_pipe(name, *args): ...
def find_pg_tool(name): ...
def exec_pg_environ(): ...
def exec_pg_command(name, *args) -> None: ...
def exec_pg_command_pipe(name, *args): ...
def file_path(file_path, filter_ext=...): ...
def file_open(name, mode: str = ..., filter_ext: Any | None = ...): ...
def flatten(list): ...
def reverse_enumerate(l): ...
def partition(pred, elems): ...
def topological_sort(elems): ...
def merge_sequences(*iterables): ...

class PatchedWorkbook(xlwt.Workbook):
    def add_sheet(self, name, cell_overwrite_ok: bool = ...): ...

class PatchedXlsxWorkbook(xlsxwriter.Workbook):
    def add_worksheet(self, name: Any | None = ..., **kw): ...

def to_xml(s): ...
def get_iso_codes(lang): ...
def scan_languages(): ...
def mod10r(number): ...
def str2bool(s, default: Any | None = ...): ...
def human_size(sz): ...
def logged(f): ...

class profile:
    fname: Any
    def __init__(self, fname: Any | None = ...) -> None: ...
    def __call__(self, f): ...

def detect_ip_addr(): ...

DEFAULT_SERVER_DATE_FORMAT: str
DEFAULT_SERVER_TIME_FORMAT: str
DEFAULT_SERVER_DATETIME_FORMAT: Any
DATE_LENGTH: Any
DATETIME_FORMATS_MAP: Any
POSIX_TO_LDML: Any

def posix_to_ldml(fmt, locale): ...
def split_every(n, iterable, piece_maker=...) -> None: ...
def get_and_group_by_field(cr, uid, obj, ids, field, context: Any | None = ...): ...
def get_and_group_by_company(cr, uid, obj, ids, context: Any | None = ...): ...
def resolve_attr(obj, attr): ...
def attrgetter(*items): ...
def discardattr(obj, key) -> None: ...
def remove_accents(input_str): ...

class unquote(str):
    def __repr__(self): ...

class UnquoteEvalContext(defaultdict):
    def __init__(self, *args, **kwargs) -> None: ...
    def __missing__(self, key): ...

class mute_logger:
    loggers: Any
    def __init__(self, *loggers) -> None: ...
    def filter(self, record): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any | None = ..., exc_val: Any | None = ..., exc_tb: Any | None = ...) -> None: ...
    def __call__(self, func): ...

_ph: Any

class CountingStream:
    stream: Any
    index: Any
    stopped: bool
    def __init__(self, stream, start: int = ...) -> None: ...
    def __iter__(self): ...
    def next(self): ...
    __next__: Any

def stripped_sys_argv(*strip_args): ...

class ConstantMapping(Mapping):
    __slots__: Any
    _value: Any
    def __init__(self, val) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, item): ...

def dumpstacks(sig: Any | None = ..., frame: Any | None = ..., thread_idents: Any | None = ...) -> None: ...
def freehash(arg): ...
def clean_context(context): ...

class frozendict(dict):
    __slots__: Any
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, val) -> None: ...
    def clear(self) -> None: ...
    def pop(self, key, default: Any | None = ...) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, key, default: Any | None = ...) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def __hash__(self): ...

class Collector(dict):
    __slots__: Any
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def add(self, key, val) -> None: ...

class StackMap(MutableMapping):
    __slots__: Any
    _maps: Any
    def __init__(self, m: Any | None = ...) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def __str__(self): ...
    def pushmap(self, m: Any | None = ...) -> None: ...
    def popmap(self): ...

class OrderedSet(MutableSet):
    __slots__: Any
    _map: Any
    def __init__(self, elems=...) -> None: ...
    def __contains__(self, elem): ...
    def __iter__(self): ...
    def __len__(self): ...
    def add(self, elem) -> None: ...
    def discard(self, elem) -> None: ...
    def update(self, elems) -> None: ...
    def difference_update(self, elems) -> None: ...
    def __repr__(self): ...

class LastOrderedSet(OrderedSet):
    def add(self, elem) -> None: ...

class Callbacks:
    __slots__: Any
    _funcs: Any
    data: Any
    def __init__(self) -> None: ...
    def add(self, func) -> None: ...
    def run(self) -> None: ...
    def clear(self) -> None: ...

class IterableGenerator:
    __slots__: Any
    func: Any
    args: Any
    def __init__(self, func, *args) -> None: ...
    def __iter__(self): ...

def groupby(iterable, key: Any | None = ...): ...
def unique(it) -> None: ...

class Reverse:
    __slots__: Any
    val: Any
    def __init__(self, val) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...

def ignore(*exc) -> None: ...

html_escape: Any

def get_lang(env, lang_code: bool = ...): ...
def babel_locale_parse(lang_code): ...
def formatLang(env, value, digits: Any | None = ..., grouping: bool = ..., monetary: bool = ..., dp: bool = ..., currency_obj: bool = ...): ...
def format_date(env, value, lang_code: bool = ..., date_format: bool = ...): ...
def parse_date(env, value, lang_code: bool = ...): ...
def format_datetime(env, value, tz: bool = ..., dt_format: str = ..., lang_code: bool = ...): ...
def format_time(env, value, tz: bool = ..., time_format: str = ..., lang_code: bool = ...): ...
def _format_time_ago(env, time_delta, lang_code: bool = ..., add_direction: bool = ...): ...
def format_decimalized_number(number, decimal: int = ...): ...
def format_decimalized_amount(amount, currency: Any | None = ...): ...
def format_amount(env, amount, currency, lang_code: bool = ...): ...
def format_duration(value): ...
def _consteq(str1, str2): ...

consteq: Any

class Unpickler(pickle_.Unpickler):
    find_global: Any
    find_class: Any

def _pickle_load(stream, encoding: str = ..., errors: bool = ...): ...

pickle: Any

class DotDict(dict):
    def __getattr__(self, attrib): ...

def get_diff(data_from, data_to, custom_style: bool = ...): ...
def traverse_containers(val, type_) -> None: ...
def hmac(env, scope, message, hash_function=...): ...
