from re import Pattern
from typing import Iterable, MutableSet

def transpile_javascript(url: str, content: str) -> str: ...

URL_RE: Pattern

def url_to_module_path(url: str) -> str: ...
def wrap_with_qunit_module(url: str, content: str) -> str: ...
def wrap_with_odoo_define(
    module_path: str, dependencies: Iterable[str], content: str
) -> str: ...

EXPORT_FCT_RE: Pattern

def convert_export_function(content: str) -> str: ...

EXPORT_CLASS_RE: Pattern

def convert_export_class(content: str) -> str: ...

EXPORT_FCT_DEFAULT_RE: Pattern

def convert_export_function_default(content: str):
    str: ...

EXPORT_CLASS_DEFAULT_RE: Pattern

def convert_export_class_default(content: str) -> str: ...

EXPORT_VAR_RE: Pattern

def convert_variable_export(content: str) -> str: ...

EXPORT_DEFAULT_VAR_RE: Pattern

def convert_variable_export_default(content: str) -> str: ...

EXPORT_OBJECT_RE: Pattern

def convert_object_export(content: str) -> str: ...

EXPORT_FROM_RE: Pattern

def convert_from_export(content: str) -> str: ...

EXPORT_STAR_FROM_RE: Pattern

def convert_star_from_export(content: str) -> str: ...

EXPORT_DEFAULT_RE: Pattern

def convert_default_export(content: str) -> str: ...

IMPORT_BASIC_RE: Pattern

def convert_basic_import(content: str) -> str: ...

IMPORT_LEGACY_DEFAULT_RE: Pattern

def convert_legacy_default_import(content: str) -> str: ...

IMPORT_DEFAULT: Pattern

def convert_default_import(content: str) -> str: ...

IS_PATH_LEGACY_RE: Pattern
IMPORT_DEFAULT_AND_NAMED_RE: Pattern

def convert_default_and_named_import(content: str) -> str: ...

RELATIVE_REQUIRE_RE: Pattern

def convert_relative_require(
    url: str, dependencies: MutableSet[str], content: str
) -> str: ...

IMPORT_STAR: Pattern

def convert_star_import(content: str) -> str: ...

IMPORT_DEFAULT_AND_STAR: Pattern

def convert_default_and_star_import(content: str) -> str: ...

IMPORT_UNNAMED_RELATIVE_RE: Pattern

def convert_unnamed_relative_import(content: str) -> str: ...

URL_INDEX_RE: Pattern

def remove_index(content: str) -> str: ...
def relative_path_to_module_path(url: str, path_rel: str) -> str: ...

ODOO_MODULE_RE: Pattern

def is_odoo_module(content: str) -> str: ...
def get_aliased_odoo_define_content(module_path: str, content: str) -> str: ...
def convert_as(val: str) -> list[str] | str: ...
def remove_as(val: str) -> list[str] | str: ...
