import pickle as pickle_
from collections import Mapping, MutableMapping, MutableSet
from itertools import repeat as repeat
from typing import Any, Optional

import xlsxwriter
import xlwt

from ..loglevels import exception_to_unicode as exception_to_unicode
from ..loglevels import get_encodings as get_encodings
from .cache import *

SKIPPED_ELEMENT_TYPES: Any

def find_in_path(name): ...
def exec_command_pipe(name, *args): ...
def find_pg_tool(name): ...
def exec_pg_environ(): ...
def exec_pg_command(name, *args) -> None: ...
def exec_pg_command_pipe(name, *args): ...
def file_open(name, mode: str = ..., subdir: str = ..., pathinfo: bool = ...): ...
def flatten(list): ...
def reverse_enumerate(l): ...
def partition(pred, elems): ...
def topological_sort(elems): ...

class PatchedWorkbook(xlwt.Workbook):
    def add_sheet(self, name, cell_overwrite_ok: bool = ...): ...

class PatchedXlsxWorkbook(xlsxwriter.Workbook):
    def add_worksheet(self, name: Optional[Any] = ..., **kw): ...

def to_xml(s): ...
def get_iso_codes(lang): ...
def scan_languages(): ...
def get_user_companies(cr, user): ...
def mod10r(number): ...
def str2bool(s, default: Optional[Any] = ...): ...
def human_size(sz): ...
def logged(f): ...

class profile:
    fname: Any
    def __init__(self, fname: Optional[Any] = ...) -> None: ...
    def __call__(self, f): ...

def detect_ip_addr(): ...

DEFAULT_SERVER_DATE_FORMAT: str
DEFAULT_SERVER_TIME_FORMAT: str
DEFAULT_SERVER_DATETIME_FORMAT: Any
DATE_LENGTH: Any
DATETIME_FORMATS_MAP: Any
POSIX_TO_LDML: Any

def posix_to_ldml(fmt, locale): ...
def split_every(n, iterable, piece_maker: Any = ...) -> None: ...
def get_and_group_by_field(cr, uid, obj, ids, field, context: Optional[Any] = ...): ...
def get_and_group_by_company(cr, uid, obj, ids, context: Optional[Any] = ...): ...
def resolve_attr(obj, attr): ...
def attrgetter(*items): ...
def remove_accents(input_str): ...

class unquote(str): ...

class UnquoteEvalContext(defaultdict):
    def __init__(self, *args, **kwargs) -> None: ...
    def __missing__(self, key): ...

class mute_logger:
    loggers: Any
    def __init__(self, *loggers) -> None: ...
    def filter(self, record): ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: Optional[Any] = ...,
        exc_val: Optional[Any] = ...,
        exc_tb: Optional[Any] = ...,
    ) -> None: ...
    def __call__(self, func): ...

class CountingStream:
    stream: Any
    index: Any
    stopped: bool
    def __init__(self, stream, start: int = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def next(self): ...
    __next__: Any

def stripped_sys_argv(*strip_args): ...

class ConstantMapping(Mapping):
    def __init__(self, val) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, item): ...

def dumpstacks(
    sig: Optional[Any] = ...,
    frame: Optional[Any] = ...,
    thread_idents: Optional[Any] = ...,
) -> None: ...
def freehash(arg): ...
def clean_context(context): ...

class frozendict(dict):
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, val) -> None: ...
    def clear(self) -> None: ...
    def pop(self, key, default: Optional[Any] = ...) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, key, default: Optional[Any] = ...) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def __hash__(self) -> Any: ...

class Collector(Mapping):
    def __init__(self) -> None: ...
    def add(self, key, val) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...

class StackMap(MutableMapping):
    def __init__(self, m: Optional[Any] = ...) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def pushmap(self, m: Optional[Any] = ...) -> None: ...
    def popmap(self): ...

class OrderedSet(MutableSet):
    def __init__(self, elems: Any = ...) -> None: ...
    def __contains__(self, elem): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def add(self, elem) -> None: ...
    def discard(self, elem) -> None: ...

class LastOrderedSet(OrderedSet):
    def add(self, elem) -> None: ...

def groupby(iterable, key: Optional[Any] = ...): ...
def unique(it) -> None: ...

class Reverse:
    val: Any
    def __init__(self, val) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...

def ignore(*exc) -> None: ...
def html_escape(text): ...
def formatLang(
    env,
    value,
    digits: Optional[Any] = ...,
    grouping: bool = ...,
    monetary: bool = ...,
    dp: bool = ...,
    currency_obj: bool = ...,
): ...
def format_date(env, value, lang_code: str = ..., date_format: bool = ...): ...

consteq: Any

class Unpickler(pickle_.Unpickler):
    find_global: Any
    find_class: Any

pickle: Any

def wrap_module(module, attr_list): ...

class DotDict(dict):
    def __getattr__(self, attrib): ...

def traverse_containers(val, type_) -> None: ...
