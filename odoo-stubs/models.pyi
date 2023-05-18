from collections import defaultdict
from re import Pattern
from typing import (
    Any,
    Callable,
    Collection,
    Container,
    Iterable,
    Iterator,
    Literal,
    MutableMapping,
    Sequence,
    TypeVar,
    Union,
    overload,
)

import psycopg2
from lxml.etree import _Element

from . import api, fields
from .api import Environment
from .fields import Field
from .modules.registry import Registry
from .osv.query import Query
from .sql_db import Cursor

_T = TypeVar("_T")
_ModelT = TypeVar("_ModelT", bound=BaseModel)
_Domain = list

regex_order: Pattern[str]
regex_object_name: Pattern[str]
regex_pg_name: Pattern[str]
regex_field_agg: Pattern[str]
AUTOINIT_RECALCULATE_STORED_FIELDS: int

def check_object_name(name: str) -> bool: ...
def raise_on_invalid_object_name(name: str) -> None: ...
def check_pg_name(name: str) -> None: ...

regex_private: Pattern[str]

def check_method_name(name: str) -> None: ...
def same_name(f, g) -> bool: ...
def fix_import_export_id_paths(fieldname: str) -> list[str]: ...
def trigger_tree_merge(node1: dict, node2: dict) -> None: ...

class MetaModel(api.Meta):
    module_to_models: defaultdict[str, list[type[BaseModel]]]
    def __new__(meta, name: str, bases: tuple, attrs: dict): ...
    def __init__(
        self: type[BaseModel], name: str, bases: tuple, attrs: dict
    ) -> None: ...

class NewId:
    __slots__: list[str]
    origin: int | None
    ref: Any
    def __init__(self, origin: int | None = ..., ref: Any | None = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

def origin_ids(ids: Iterable) -> Iterator[int]: ...
def expand_ids(id0: _T, ids: Iterable) -> Iterator[_T]: ...

IdType: tuple[type[int], type[str], type[NewId]]
PREFETCH_MAX: int
LOG_ACCESS_COLUMNS: list[str]
MAGIC_COLUMNS: list[str]
VALID_AGGREGATE_FUNCTIONS: set[str]

class BaseModel(metaclass=MetaModel):
    __slots__: list[str]
    _auto: bool
    _register: bool
    _abstract: bool
    _transient: bool
    _name: str
    _description: str
    _custom: bool
    _inherit: str | list[str]
    _inherits: dict[str, str]
    _table: str
    _table_query: str | None
    _sequence: str | None
    _sql_constraints: list[tuple[str, str, str]]
    _rec_name: str | None
    _order: str
    _parent_name: str
    _parent_store: bool
    _active_name: str | None
    _date_name: str
    _fold_name: str
    _needaction: bool
    _translate: bool
    _check_company_auto: bool
    _depends: dict[str, Iterable[str]]
    _transient_max_count: int
    _transient_max_hours: float
    _original_module: str
    _inherit_module: dict[str, str]
    _inherit_children: set[str]
    _inherits_children: set[str]
    _fields: dict[str, Field]
    _field_definitions: list[Field]
    _log_access: bool
    _ids: tuple
    _prefetch_ids: Iterable[int]
    __base_classes: tuple[type[BaseModel] | type, ...]
    env: Environment = ...
    pool: Registry
    id = fields.Id()
    display_name = fields.Char(string="Display Name")
    create_uid = fields.Many2one("res.users", string="Created by")
    create_date = fields.Datetime(string="Created on")
    write_uid = fields.Many2one("res.users", string="Last Updated by")
    write_date = fields.Datetime(string="Last Updated on")
    CONCURRENCY_CHECK_FIELD: str
    def view_init(self, fields_list: list[str]) -> None: ...
    def _valid_field_parameter(self, field: Field, name: str) -> bool: ...
    def _add_field(self, name: str, field: Field) -> None: ...
    def _pop_field(self, name: str) -> Field: ...
    def _add_magic_fields(self) -> None: ...
    def compute_concurrency_field(self) -> None: ...
    def compute_concurrency_field_with_access(self) -> None: ...
    @classmethod
    def _build_model(cls, pool: Registry, cr: Cursor) -> BaseModel: ...
    @classmethod
    def _build_model_check_base(model_class, cls: type[BaseModel]) -> None: ...
    @classmethod
    def _build_model_check_parent(
        model_class, cls: type[BaseModel], parent_class: type[BaseModel]
    ) -> None: ...
    @classmethod
    def _build_model_attributes(cls, pool: Registry) -> None: ...
    @classmethod
    def _init_constraints_onchanges(cls) -> None: ...
    @property
    def _constraint_methods(self) -> list: ...
    @property
    def _onchange_methods(self) -> dict[str, list]: ...
    def __new__(cls) -> None: ...
    def __init__(self, pool: Registry, cr: Cursor) -> None: ...
    def _is_an_ordinary_table(self) -> bool: ...
    def __ensure_xml_id(
        self: _ModelT, skip: bool = ...
    ) -> Iterator[tuple[_ModelT, str | None]]: ...
    def _export_rows(
        self, fields: list[list[str]], *, _is_toplevel_call: bool = ...
    ) -> list[list]: ...
    __export_rows = _export_rows
    def export_data(self, fields_to_export: list[str]) -> dict[str, list[list]]: ...
    def load(self, fields: list[str], data: list[list[str]]) -> dict[str, Any]: ...
    def _add_fake_fields(
        self, fields: dict[str | None, Field]
    ) -> dict[str | None, Field]: ...
    def _extract_records(
        self,
        fields_: Iterable[Sequence[str]],
        data,
        log: Callable = ...,
        limit: float = ...,
    ) -> Iterator[tuple[BaseModel, dict[str, dict[str, int]]]]: ...
    def _convert_records(
        self, records, log: Callable = ...
    ) -> Iterator[tuple[Any, Any, Any, dict]]: ...
    def _validate_fields(
        self, field_names: Iterable[str], excluded_names: Iterable[str] = ...
    ) -> None: ...
    def default_get(self, fields_list: list[str]) -> dict[str, Any]: ...
    def fields_get_keys(self) -> list[str]: ...
    def _rec_name_fallback(self) -> str: ...
    def view_header_get(self, view_id: Any | None = ..., view_type: str = ...): ...
    def user_has_groups(self, groups: str) -> bool: ...
    def _get_default_form_view(self) -> _Element: ...
    def _get_default_search_view(self) -> _Element: ...
    def _get_default_tree_view(self) -> _Element: ...
    def _get_default_pivot_view(self) -> _Element: ...
    def _get_default_kanban_view(self) -> _Element: ...
    def _get_default_graph_view(self) -> _Element: ...
    def _get_default_calendar_view(self) -> _Element: ...
    def load_views(self, views: list, options: dict | None = ...) -> dict[str, Any]: ...
    def _fields_view_get(
        self,
        view_id: int | None = ...,
        view_type: str = ...,
        toolbar: bool = ...,
        submenu: bool = ...,
    ) -> dict[str, Any]: ...
    def fields_view_get(
        self,
        view_id: int | None = ...,
        view_type: str = ...,
        toolbar: bool = ...,
        submenu: bool = ...,
    ) -> dict[str, Any]: ...
    def get_formview_id(self, access_uid: int | None = ...): ...
    def get_formview_action(self, access_uid: int | None = ...) -> dict[str, Any]: ...
    def get_access_action(self, access_uid: int | None = ...) -> dict[str, Any]: ...
    def search_count(self, args: _Domain) -> int: ...
    @overload
    def search(
        self: _ModelT,
        args: _Domain,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
        count: Literal[False] = ...,
    ) -> _ModelT: ...
    @overload
    def search(
        self: _ModelT,
        args: _Domain,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
        count: Literal[True] = ...,
    ) -> int: ...
    def _compute_display_name(self) -> None: ...
    def name_get(self) -> list[tuple[int, str]]: ...
    def name_create(self, name: str) -> tuple[int, str]: ...
    def name_search(
        self,
        name: str = ...,
        args: _Domain | None = ...,
        operator: str = ...,
        limit: int = ...,
    ) -> list[tuple[int, str]]: ...
    def _name_search(
        self,
        name: str = ...,
        args: _Domain | None = ...,
        operator: str = ...,
        limit: int = ...,
        name_get_uid: int | None = ...,
    ) -> list[int]: ...
    def _add_missing_default_values(self, values: dict[str, Any]) -> dict[str, Any]: ...
    @classmethod
    def clear_caches(cls) -> None: ...
    def _read_group_expand_full(
        self, groups: _ModelT, domain: _Domain | None, order: str | None
    ) -> _ModelT: ...
    def _read_group_fill_results(
        self,
        domain: _Domain,
        groupby: str,
        remaining_groupbys: list[str],
        aggregated_fields: list[str],
        count_field: str,
        read_group_result,
        read_group_order: str | None = ...,
    ) -> list: ...
    def _read_group_fill_temporal(
        self,
        data: list,
        groupby: list[str],
        aggregated_fields: list[str],
        annotated_groupbys: list[dict],
        interval=...,
    ) -> list: ...
    def _read_group_prepare(
        self,
        orderby: str,
        aggregated_fields: list[str],
        annotated_groupbys: list[dict],
        query: Query,
    ) -> tuple[list, list]: ...
    def _read_group_process_groupby(self, gb: str, query: Query) -> dict[str, Any]: ...
    def _read_group_prepare_data(
        self, key, value, groupby_dict: dict[str, dict[str, Any]]
    ) -> Any: ...
    def _read_group_format_result(
        self, data: dict, annotated_groupbys: list[dict], groupby: list, domain: _Domain
    ) -> dict: ...
    def read_group(
        self,
        domain: _Domain,
        fields: list[str],
        groupby: str | list[str],
        offset: int = ...,
        limit: int | None = ...,
        orderby: str | None = ...,
        lazy: bool = ...,
    ) -> list[dict[str, Any]]: ...
    def _read_group_raw(
        self,
        domain: _Domain,
        fields: list[str],
        groupby: str | list[str],
        offset: int = ...,
        limit: int | None = ...,
        orderby: str | None = ...,
        lazy: bool = ...,
    ) -> list[dict[str, Any]]: ...
    def _read_group_resolve_many2one_fields(
        self, data: list[dict[str, Any]], fields: list[dict[str, Any]]
    ) -> None: ...
    def _inherits_join_add(
        self, current_model: BaseModel, parent_model_name: str, query: Query
    ) -> str: ...
    def _inherits_join_calc(self, alias: str, fname: str, query: Query) -> str: ...
    def _parent_store_compute(self): ...
    def _check_removed_columns(self, log: bool = ...) -> None: ...
    def _init_column(self, column_name: str) -> None: ...
    def _table_has_rows(self) -> int: ...
    def _auto_init(self): ...
    def init(self) -> None: ...
    def _create_parent_columns(self) -> None: ...
    def _add_sql_constraints(self) -> None: ...
    def _execute_sql(self) -> None: ...
    def _add_inherited_fields(self) -> None: ...
    def _inherits_check(self) -> None: ...
    def _prepare_setup(self) -> None: ...
    def _setup_base(self) -> None: ...
    def _setup_fields(self) -> None: ...
    def _setup_complete(self) -> None: ...
    def fields_get(
        self, allfields: list[str] | None = ..., attributes: list[str] | None = ...
    ) -> dict[str, dict[str, Any]]: ...
    def get_empty_list_help(self, help: str) -> str: ...
    def check_field_access_rights(self, operation: str, fields: Collection[str]): ...
    def read(
        self, fields: Collection[str] | None = ..., load: str = ...
    ) -> list[dict[str, Any]]: ...
    def _read_format(
        self, fnames: Collection[str], load: str = ...
    ) -> list[dict[str, Any]]: ...
    def _fetch_field(self, field: Field) -> None: ...
    def _read(self, fields: Collection[str]): ...
    def get_metadata(self) -> list[dict[str, Any]]: ...
    def get_base_url(self) -> str: ...
    def _check_concurrency(self) -> None: ...
    def _check_company(self, fnames: Collection[str] | None = ...) -> None: ...
    def check_access_rights(
        self, operation: str, raise_exception: bool = ...
    ) -> bool: ...
    def check_access_rule(self, operation: str) -> None: ...
    def _filter_access_rules(self: _ModelT, operation: str) -> _ModelT: ...
    def _filter_access_rules_python(self, operation: str) -> _ModelT: ...
    def unlink(self): ...
    def write(self, vals: dict[str, Any]): ...
    def _write(self, vals: dict[str, Any]): ...
    def create(
        self: _ModelT, vals_list: list[dict[str, Any]] | dict[str, Any]
    ) -> _ModelT: ...
    def _create(self: _ModelT, data_list: list[dict[str, Any]]) -> _ModelT: ...
    def _compute_field_value(self, field: Field) -> None: ...
    def _parent_store_create(self) -> None: ...
    def _parent_store_update_prepare(self: _ModelT, vals: dict) -> _ModelT: ...
    def _parent_store_update(self) -> None: ...
    def _load_records_write(self, values: dict[str, Any]) -> None: ...
    def _load_records_create(self, values: list[dict[str, Any]]): ...
    def _load_records(self, data_list: list[dict], update: bool = ...) -> BaseModel: ...
    def _where_calc(self, domain: _Domain, active_test: bool = ...) -> Query: ...
    def _check_qorder(self, word: str) -> bool: ...
    def _apply_ir_rules(self, query: Query, mode: str = ...) -> None: ...
    def _generate_translated_field(
        self, table_alias: str, field: str, query: Query
    ) -> str: ...
    def _generate_m2o_order_by(
        self,
        alias: str,
        order_field: str,
        query: Query,
        reverse_direction: bool,
        seen: set | None,
    ) -> list[str]: ...
    def _generate_order_by_inner(
        self,
        alias: str,
        order_spec: str,
        query: Query,
        reverse_direction: bool = ...,
        seen: set | None = ...,
    ) -> list[str]: ...
    def _generate_order_by(self, order_spec: str | None, query: Query) -> str: ...
    def _flush_search(
        self,
        domain: _Domain,
        fields: Sequence[str] | None = ...,
        order: str | None = ...,
        seen: set | None = ...,
    ) -> None: ...
    def _search(
        self: _ModelT,
        args: _Domain,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
        count: bool = ...,
        access_rights_uid: int | None = ...,
    ) -> Query | int: ...
    def copy_data(
        self, default: dict[str, Any] | None = ...
    ) -> list[dict[str, Any]]: ...
    def copy_translations(
        old: _ModelT, new: _ModelT, excluded: Container[str] = ...
    ) -> None: ...
    def copy(self: _ModelT, default: dict[str, Any] | None = ...) -> _ModelT: ...
    def exists(self: _ModelT) -> _ModelT: ...
    def _check_recursion(self, parent: str | None = ...) -> bool: ...
    def _check_m2m_recursion(self, field_name: str) -> bool: ...
    def _get_external_ids(self) -> dict[int, list[str]]: ...
    def get_external_id(self) -> dict[int, str]: ...
    get_xml_id = get_external_id
    _get_xml_ids = _get_external_ids
    @classmethod
    def is_transient(cls) -> bool: ...
    def search_read(
        self,
        domain: _Domain | None = ...,
        fields: list[str] | None = ...,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
    ) -> list[dict[str, Any]]: ...
    def toggle_active(self) -> None: ...
    def action_archive(self): ...
    def action_unarchive(self): ...
    def _register_hook(self) -> None: ...
    def _unregister_hook(self) -> None: ...
    @classmethod
    def _patch_method(cls, name: str, method) -> None: ...
    @classmethod
    def _revert_method(cls, name: str) -> None: ...
    @classmethod
    def _browse(
        cls: type[_ModelT], env: Environment, ids: tuple, prefetch_ids: Iterable[int]
    ) -> _ModelT: ...
    def browse(
        self: _ModelT, ids: int | NewId | Iterable[int | NewId] | None = ...
    ) -> _ModelT: ...
    @property
    def ids(self) -> list[int]: ...
    _cr: Cursor
    _uid: int
    _context: dict
    def ensure_one(self: _ModelT) -> _ModelT: ...
    def with_env(self: _ModelT, env: Environment) -> _ModelT: ...
    def sudo(self: _ModelT, flag: bool = ...) -> _ModelT: ...
    def with_user(
        self: _ModelT, user: Union["odoo.model.res_partner", int]
    ) -> _ModelT: ...
    def with_company(
        self: _ModelT, company: Union["odoo.model.res_company", int]
    ) -> _ModelT: ...
    def with_context(self: _ModelT, *args, **kwargs) -> _ModelT: ...
    def with_prefetch(
        self: _ModelT, prefetch_ids: Iterable[int] | None = ...
    ) -> _ModelT: ...
    def _update_cache(self, values: dict[str, Any], validate: bool = ...): ...
    def _convert_to_record(self, values: dict[str, Any]): ...
    def _convert_to_write(self, values: dict[str, Any]) -> dict[str, Any]: ...
    def _mapped_func(self, func: Callable): ...
    def mapped(self, func: Callable | str): ...
    def _mapped_cache(self, name_seq: str): ...
    def filtered(self: _ModelT, func: Callable | str) -> _ModelT: ...
    def filtered_domain(self: _ModelT, domain: _Domain) -> _ModelT: ...
    def sorted(
        self: _ModelT, key: Callable | str | None = ..., reverse: bool = ...
    ) -> _ModelT: ...
    def update(self, values: dict[str, Any]) -> None: ...
    def flush(
        self, fnames: Collection[str] | None = ..., records: BaseModel | None = ...
    ) -> None: ...
    def new(
        self: _ModelT,
        values: dict[str, Any] = ...,
        origin: _ModelT | None = ...,
        ref: Any | None = ...,
    ) -> _ModelT: ...
    @property
    def _origin(self: _ModelT) -> _ModelT: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self: _ModelT) -> Iterator[_ModelT]: ...
    def __contains__(self: _ModelT, item: _ModelT | str) -> bool: ...
    def __add__(self: _ModelT, other: _ModelT) -> _ModelT: ...
    def concat(self: _ModelT, *args: _ModelT) -> _ModelT: ...
    def __sub__(self: _ModelT, other: _ModelT) -> _ModelT: ...
    def __and__(self: _ModelT, other: _ModelT) -> _ModelT: ...
    def __or__(self: _ModelT, other: _ModelT) -> _ModelT: ...
    def union(self: _ModelT, *args: _ModelT) -> _ModelT: ...
    def __eq__(self: _ModelT, other: _ModelT) -> bool: ...
    def __lt__(self: _ModelT, other: _ModelT) -> bool: ...
    def __le__(self: _ModelT, other: _ModelT) -> bool: ...
    def __gt__(self: _ModelT, other: _ModelT) -> bool: ...
    def __ge__(self: _ModelT, other: _ModelT) -> bool: ...
    def __int__(self): ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __getitem__(self, key: str | int | slice): ...
    def __setitem__(self, key: str, value): ...
    @property
    def _cache(self) -> RecordCache: ...
    def _in_cache_without(self: _ModelT, field: Field, limit: int = ...) -> _ModelT: ...
    def refresh(self) -> None: ...
    def invalidate_cache(
        self, fnames: Collection[str] | None = ..., ids: Iterable[int] | None = ...
    ) -> None: ...
    def modified(
        self, fnames: Collection[str], create: bool = ..., before: bool = ...
    ) -> None: ...
    def _modified_triggers(
        self: _ModelT, tree: dict[Field | None, Any], create: bool = ...
    ) -> Iterator[tuple[Field, _ModelT, bool]]: ...
    def recompute(
        self,
        fnames: Collection[str] | None = ...,
        records: Union[BaseModel, None] = ...,
    ) -> None: ...
    def _dependent_fields(self, field: Field) -> Iterator[Field]: ...
    def _has_onchange(self, field: Field, other_fields: Container[Field]) -> bool: ...
    def _onchange_spec(self, view_info: dict | None = ...) -> dict: ...
    def _onchange_eval(self, field_name: str, onchange: str, result: dict) -> None: ...
    def onchange(
        self,
        values: dict[str, Any],
        field_name: str | list[str] | bool,
        field_onchange: dict[str, str],
    ) -> dict: ...
    def _get_placeholder_filename(self, field: str) -> str | bool: ...
    def _populate_factories(self) -> list[tuple[str, Callable[..., Iterator]]]: ...
    @property
    def _populate_sizes(self) -> dict[str, int]: ...
    @property
    def _populate_dependencies(self) -> list[str]: ...
    def _populate(self: _ModelT, size: str) -> _ModelT: ...

class RecordCache(MutableMapping):
    _record: BaseModel
    def __init__(self, record: BaseModel) -> None: ...
    def __contains__(self, name: str) -> bool: ...
    def __getitem__(self, name: str) -> Any: ...
    def __setitem__(self, name: str, value: Any) -> None: ...
    def __delitem__(self, name: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...

AbstractModel = BaseModel

class Model(AbstractModel):
    _auto: bool
    _register: bool
    _abstract: bool
    _transient: bool

class TransientModel(Model):
    _auto: bool
    _register: bool
    _abstract: bool
    _transient: bool
    def _transient_vacuum(self) -> None: ...
    def _transient_clean_old_rows(self, max_count: int) -> None: ...
    def _transient_clean_rows_older_than(self, seconds) -> None: ...

def itemgetter_tuple(items) -> Callable[..., tuple]: ...
def convert_pgerror_not_null(
    model: BaseModel, fields: dict[str, dict[str, Any]], info, e: psycopg2.Error
) -> dict[str, str]: ...
def convert_pgerror_unique(
    model: BaseModel, fields: dict[str, dict[str, Any]], info, e: psycopg2.Error
) -> dict[str, str]: ...
def convert_pgerror_constraint(
    model: BaseModel, fields: dict[str, dict[str, Any]], info, e: psycopg2.Error
) -> dict[str, str]: ...

PGERROR_TO_OE: dict[str, Callable]

def lazy_name_get(self: BaseModel) -> list[tuple[int, str]]: ...
