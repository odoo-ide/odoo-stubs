import collections
from concurrent.futures import Future
from contextlib import contextmanager
from itertools import count
from subprocess import Popen
from typing import Any, Callable, Generator, Mapping, Match, TypeVar
from xmlrpc import client as xmlrpclib

import requests
from odoo.addons.base.models.res_users import Users
from websocket import WebSocket

from ..api import Environment
from ..http import Session
from ..models import BaseModel
from ..modules.registry import Registry
from ..sql_db import BaseCursor, Cursor
from ..tools import mute_logger, profiler
from ..tools._vendor.sessions import Session
from ..tools.profiler import Profiler
from . import case
from .form import Form as Form
from .result import OdooTestResult

_T = TypeVar("_T")
_CallableT = TypeVar("_CallableT", bound=Callable)

InvalidStateError = Any
ADDONS_PATH: str
HOST: str
ADMIN_USER_ID: int
CHECK_BROWSER_SLEEP: float
CHECK_BROWSER_ITERATIONS: int
BROWSER_WAIT: float
DEFAULT_SUCCESS_SIGNAL: str

def get_db_name() -> str: ...

standalone_tests: collections.defaultdict[str, list]

def standalone(*tags: str) -> Callable[[_CallableT], _CallableT]: ...

DB: str

def new_test_user(
    env: Environment,
    login: str = ...,
    groups: str = ...,
    context: dict | None = ...,
    **kwargs
) -> Users: ...
def loaded_demo_data(env: Environment) -> bool: ...

class RecordCapturer:
    def __init__(self, model: BaseModel, domain: list) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None: ...
    @property
    def records(self) -> BaseModel: ...

class MetaCase(type):
    def __init__(cls, name, bases, attrs) -> None: ...

class BlockedRequest(requests.exceptions.ConnectionError): ...

class BaseCase(case.TestCase, metaclass=MetaCase):
    registry: Registry
    env: Environment
    cr: Cursor
    longMessage: bool
    warm: bool
    def __init__(self, methodName: str = ...) -> None: ...
    def run(self, result: OdooTestResult) -> None: ...
    def cursor(self) -> Cursor: ...
    @property
    def uid(self) -> int: ...
    @uid.setter
    def uid(self, user) -> None: ...
    def ref(self, xid: str) -> int: ...
    def browse_ref(self, xid: str) -> BaseModel | None: ...
    def patch(self, obj, key, val) -> None: ...
    @classmethod
    def classPatch(cls, obj, key, val) -> None: ...
    def startPatcher(self, patcher): ...
    @classmethod
    def startClassPatcher(cls, patcher): ...
    def with_user(self, login: str) -> None: ...
    def debug_mode(self) -> Generator[None, None, None]: ...
    @contextmanager
    def assertRaises(
        self, exception, func: Any | None = ..., *args, **kwargs
    ) -> Generator[Any, None, None] | None: ...
    @contextmanager
    def assertQueries(
        self, expected, flush: bool = ...
    ) -> Generator[list, None, None]: ...
    @contextmanager
    def assertQueryCount(
        self, default: int = ..., flush: bool = ..., **counters
    ) -> Generator[None, None, None]: ...
    def assertRecordValues(
        self, records: BaseModel, expected_values: list[dict[str, Any]]
    ) -> None: ...
    def assertItemsEqual(self, a, b, msg: str | None = ...) -> None: ...
    def assertTreesEqual(self, n1, n2, msg: str | None = ...) -> None: ...
    def assertXMLEqual(self, original: str, expected: str) -> None: ...
    def assertHTMLEqual(self, original: str, expected: str) -> None: ...
    profile_session: str
    def profile(self, description: str = ..., **kwargs) -> Profiler: ...

class Like:
    pattern: str
    regex: str
    def __init__(self, pattern) -> None: ...

savepoint_seq: count[int]

class TransactionCase(BaseCase):
    registry: Registry
    env: Environment
    cr: Cursor
    muted_registry_logger: mute_logger
    @classmethod
    def setUpClass(cls) -> None: ...
    def setUp(self) -> None: ...

class SingleTransactionCase(BaseCase):
    @classmethod
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    def setUp(self) -> None: ...

class ChromeBrowserException(Exception): ...

def run(gen_func) -> None: ...
def save_test_file(
    test_name: str,
    content,
    prefix: str,
    extension: str = ...,
    logger=...,
    document_type: str = ...,
    date_format: str = ...,
) -> None: ...

class ChromeBrowser:
    remote_debugging_port: int
    test_case: HttpCase
    success_signal: str
    chrome: Popen
    devtools_port: int | None
    ws: WebSocket | None
    user_data_dir: str
    screencasts_dir: str | None
    screencast_frames: list
    sigxcpu_handler: Any
    error_checker: Any
    had_failure: bool
    def __init__(
        self,
        test_case: HttpCase,
        success_signal: str,
        headless: bool = ...,
        debug: bool = ...,
    ) -> None: ...
    @property
    def screencasts_frames_dir(self) -> str: ...
    def signal_handler(self, sig, frame) -> None: ...
    def stop(self) -> None: ...
    @property
    def executable(self) -> str | None: ...
    def take_screenshot(self, prefix: str = ...) -> Future: ...
    def start_screencast(self) -> None: ...
    def stop_screencast(self) -> None: ...
    def set_cookie(self, name: str, value, path, domain) -> None: ...
    def delete_cookie(self, name: str, **kwargs) -> None: ...
    def navigate_to(self, url: str, wait_stop: bool = ...) -> None: ...
    LINE_PATTERN: str
    def console_formatter(self, args: list) -> Callable[[Match[str]], str]: ...

class Opener(requests.Session):
    cr: BaseCursor
    def __init__(self, cr: BaseCursor) -> None: ...
    def request(self, *args, **kwargs): ...

class Transport(xmlrpclib.Transport):
    cr: BaseCursor
    def __init__(self, cr: BaseCursor) -> None: ...
    def request(self, *args, **kwargs): ...

class JsonRpcException(Exception):
    code: Any
    def __init__(self, code, message) -> None: ...

class HttpCase(TransactionCase):
    registry_test_mode: bool
    browser: ChromeBrowser | None
    browser_size: str
    touch_enabled: bool
    allow_end_on_form: bool
    @classmethod
    def setUpClass(cls) -> None: ...
    xmlrpc_common: xmlrpclib.ServerProxy
    xmlrpc_db: xmlrpclib.ServerProxy
    xmlrpc_object: xmlrpclib.ServerProxy
    opener: Opener
    def setUp(self) -> None: ...
    def url_open(
        self,
        url: str,
        data: Any | None = ...,
        files: Mapping | None = ...,
        timeout: int = ...,
        headers: Mapping | None = ...,
        allow_redirects: bool = ...,
        head: bool = ...,
    ) -> requests.Response: ...
    def logout(self, keep_db: bool = ...) -> None: ...
    session: Session
    def authenticate(self, user, password, browser: ChromeBrowser = ...) -> Session: ...
    def browser_js(
        self,
        url_path: str,
        code: str,
        ready: str = ...,
        login: str | None = ...,
        timeout: int = ...,
        cookies: Any | None = ...,
        error_checker: Any | None = ...,
        watch: bool = ...,
        success_signal: str = ...,
        debug: bool = ...,
        **kw
    ) -> None: ...
    @classmethod
    def base_url(cls) -> str: ...
    def start_tour(
        self, url_path: str, tour_name: str, step_delay: float | None = ..., **kwargs
    ) -> None: ...
    def profile(self, **kwargs) -> profiler.Nested: ...
    def make_jsonrpc_request(
        self, route: str, params: dict | None = ..., headers: dict | None = ...
    ): ...

def no_retry(arg: _T) -> _T: ...
def users(*logins: str) -> Callable[[_CallableT], _CallableT]: ...
def warmup(func: _CallableT, *args, **kwargs) -> _CallableT: ...
def can_import(module: str) -> bool: ...
def tagged(*tags: str) -> Callable[[_CallableT], _CallableT]: ...
