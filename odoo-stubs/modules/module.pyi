from types import ModuleType
from typing import Any, Literal, MutableSequence

from ..tools import pycompat as pycompat

MANIFEST_NAMES: tuple[str, ...]
README: list[str]
_DEFAULT_MANIFEST: dict[str, Any]

def ad_paths() -> MutableSequence[str]: ...

loaded: list

class AddonsHook:
    def find_module(self, name: str, path: Any | None = ...) -> AddonsHook | None: ...
    def load_module(self, name: str) -> ModuleType | None: ...

class OdooHook:
    def find_module(self, name: str, path: Any | None = ...) -> OdooHook | None: ...
    def load_module(self, name: str) -> ModuleType | None: ...

class UpgradeHook:
    def find_module(self, name: str, path: Any | None = ...) -> UpgradeHook | None: ...
    def load_module(self, name: str) -> ModuleType | None: ...

def initialize_sys_path() -> None: ...
def get_module_path(
    module: str, downloaded: bool = ..., display_warning: bool = ...
) -> str | Literal[False]: ...
def get_module_filetree(module: str, dir: str = ...) -> dict: ...
def get_resource_path(module: str, *args) -> str | Literal[False]: ...
def check_resource_path(mod_path: str, *args) -> str | Literal[False]: ...

get_module_resource = get_resource_path

def get_resource_from_path(path: str) -> tuple[str, str, str] | None: ...
def get_module_icon(module: str) -> str: ...
def module_manifest(path: str) -> str | None: ...
def get_module_root(path: str) -> str | None: ...
def load_manifest(module: str, mod_path: str | None = ...) -> dict[str, Any]: ...
def get_manifest(module: str, mod_path: str | None = ...) -> dict[str, Any]: ...
def load_information_from_description_file(
    module: str, mod_path: str | None = ...
) -> dict: ...
def load_openerp_module(module_name: str) -> None: ...
def get_modules() -> list[str]: ...
def get_modules_with_version() -> dict[str, Any]: ...
def adapt_version(version: str) -> str: ...

current_test: Any
