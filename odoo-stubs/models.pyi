from collections import defaultdict
from re import Pattern
from typing import (
    Any,
    Callable,
    Collection,
    Container,
    Iterable,
    Iterator,
    MutableMapping,
    Sequence,
    TypeVar,
    overload,
)

import dateutil.relativedelta
import psycopg2
from odoo.addons.base.models.res_company import Company
from odoo.addons.base.models.res_users import Users

from . import api, fields
from .api import Environment
from .fields import Field
from .modules.registry import Registry, TriggerTree
from .sql_db import Cursor
from .tools import SQL, Query

_T = TypeVar("_T")
_ModelT = TypeVar("_ModelT", bound=BaseModel)
_Model2T = TypeVar("_Model2T", bound=BaseModel)

regex_alphanumeric: Pattern[str]
regex_order: Pattern[str]
regex_object_name: Pattern[str]
regex_pg_name: Pattern[str]
regex_field_agg: Pattern[str]
regex_read_group_spec: Pattern[str]
AUTOINIT_RECALCULATE_STORED_FIELDS: int
INSERT_BATCH_SIZE: int
SQL_DEFAULT: psycopg2.extensions.AsIs

def parse_read_group_spec(spec: str) -> tuple: ...
def check_object_name(name: str) -> bool: ...
def raise_on_invalid_object_name(name: str) -> None: ...
def check_pg_name(name: str) -> None: ...

regex_private: Pattern[str]

def check_method_name(name: str) -> None: ...
def check_property_field_value_name(property_name) -> None: ...
def fix_import_export_id_paths(fieldname: str) -> list[str]: ...
def to_company_ids(companies): ...
def check_company_domain_parent_of(self, companies) -> list: ...

class MetaModel(api.Meta):
    module_to_models: defaultdict[str, list[type[BaseModel]]]
    def __new__(meta, name: str, bases: tuple, attrs: dict): ...
    def __init__(
        self: type[BaseModel], name: str, bases: tuple, attrs: dict
    ) -> None: ...

class NewId:
    origin: int | None
    ref: Any
    def __init__(self, origin: int | None = ..., ref: Any | None = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

def origin_ids(ids: Iterable) -> Iterator[int]: ...

class OriginIds:
    ids: Sequence[int]
    def __init__(self, ids: Sequence[int]) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __reversed__(self) -> Iterator[int]: ...

def expand_ids(id0: _T, ids: Iterable) -> Iterator[_T]: ...

IdType: tuple[type[int], type[NewId]]
PREFETCH_MAX: int
LOG_ACCESS_COLUMNS: list[str]
MAGIC_COLUMNS: list[str]
READ_GROUP_TIME_GRANULARITY: dict[str, dateutil.relativedelta.relativedelta]
READ_GROUP_AGGREGATE: dict[str, Callable[[str, str | SQL], SQL]]
READ_GROUP_DISPLAY_FORMAT: dict[str, str]

def is_definition_class(cls) -> bool: ...
def is_registry_class(cls) -> bool: ...

class BaseModel(metaclass=MetaModel):
    _auto: bool
    _register: bool
    _abstract: bool
    _transient: bool
    _name: str
    _description: str
    _module: str
    _custom: bool
    _inherit: str | list[str]
    _inherits: dict[str, str]
    _table: str
    _table_query: str | None
    _sql_constraints: list[tuple[str, str, str]]
    _rec_name: str | None
    _rec_names_search: Sequence[str] | None
    _order: str
    _parent_name: str
    _parent_store: bool
    _active_name: str | None
    _fold_name: str
    _translate: bool
    _check_company_auto: bool
    _allow_sudo_commands: bool
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
    _ids: tuple[int | NewId]
    _prefetch_ids: Iterable[int | NewId]
    env: Environment = ...
    pool: Registry
    id = fields.Id()
    display_name = fields.Char(string="Display Name")
    create_uid = fields.Many2one("res.users", string="Created by")
    create_date = fields.Datetime(string="Created on")
    write_uid = fields.Many2one("res.users", string="Last Updated by")
    write_date = fields.Datetime(string="Last Updated on")
    def _valid_field_parameter(self, field: Field, name: str) -> bool: ...
    def _add_field(self, name: str, field: Field) -> None: ...
    def _pop_field(self, name: str) -> Field: ...
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
    def _table_sql(self) -> SQL: ...
    @property
    def _constraint_methods(self) -> list: ...
    @property
    def _ondelete_methods(self) -> list: ...
    @property
    def _onchange_methods(self) -> dict[str, list]: ...
    def _is_an_ordinary_table(self) -> bool: ...
    def _export_rows(
        self, fields: list[list[str]], *, _is_toplevel_call: bool = ...
    ) -> list[list]: ...
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
    def _rec_name_fallback(self) -> str: ...
    def user_has_groups(self, groups: str) -> bool: ...
    def search_count(self, domain: list, limit: int | None = ...) -> int: ...
    def search(
        self: _ModelT,
        domain: list,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
    ) -> _ModelT: ...
    def search_fetch(
        self: _ModelT,
        domain: list,
        field_names: Collection[str],
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
    ) -> _ModelT: ...
    def _compute_display_name(self) -> None: ...
    def name_get(self) -> list[tuple[int, str]]: ...
    def name_create(self, name: str) -> tuple[int, str]: ...
    def name_search(
        self,
        name: str = ...,
        args: list | None = ...,
        operator: str = ...,
        limit: int = ...,
    ) -> list[tuple[int, str]]: ...
    def _name_search(
        self,
        name: str = ...,
        domain: list | None = ...,
        operator: str = ...,
        limit: int = ...,
        order: str | None = ...,
    ) -> Query: ...
    def _add_missing_default_values(self, values: dict[str, Any]) -> dict[str, Any]: ...
    @classmethod
    def clear_caches(cls) -> None: ...
    def _read_group(
        self,
        domain: list,
        groupby: Iterable[str] = ...,
        aggregates: Iterable[str] = ...,
        having: list = ...,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
    ) -> list[tuple]: ...
    def _read_group_select(self, aggregate_spec: str, query: Query) -> SQL: ...
    def _read_group_groupby(self, groupby_spec: str, query: Query) -> SQL: ...
    def _read_group_having(self, having_domain: list, query: Query) -> SQL: ...
    def _read_group_orderby(
        self, order: str, groupby_terms: dict[str, SQL], query: Query
    ) -> tuple[SQL, SQL]: ...
    def _read_group_empty_value(self, spec: str) -> Any: ...
    def _read_group_postprocess_groupby(
        self, groupby_spec: str, raw_values
    ) -> Iterator: ...
    def _read_group_postprocess_aggregate(
        self, aggregate_spec: str, raw_values
    ) -> Iterator: ...
    def _read_group_expand_full(
        self, groups: _ModelT, domain: list | None, order: str | None
    ) -> _ModelT: ...
    def _read_group_fill_results(
        self,
        domain: list,
        groupby: str,
        annoted_aggregates: dict[str, str],
        read_group_result: list[dict],
        read_group_order: str | None = ...,
    ) -> list: ...
    def _read_group_fill_temporal(
        self,
        data: list,
        groupby: list[str],
        annoted_aggregates: dict[str, str],
        fill_from: bool = ...,
        fill_to: bool = ...,
        min_groups: bool = ...,
    ) -> list: ...
    def _read_group_format_result(
        self, rows_dict: Iterable[dict], lazy_groupby: Iterable[str]
    ) -> None: ...
    def _read_group_format_result_properties(
        self, rows_dict: Iterable[dict], group: str
    ) -> None: ...
    def read_group(
        self,
        domain: list,
        fields: list[str],
        groupby: str | list[str],
        offset: int = ...,
        limit: int | None = ...,
        orderby: str | None = ...,
        lazy: bool = ...,
    ) -> list[dict[str, Any]]: ...
    def _field_to_sql(
        self, alias: str, fname: str, query: Query | None = ..., flush: bool = ...
    ) -> SQL: ...
    def _field_properties_to_sql(
        self, alias: str, fname: str, property_name: str, query: Query
    ) -> SQL: ...
    def _condition_to_sql(
        self, alias: str, fname: str, operator: str, value, query: Query
    ) -> SQL: ...
    def get_property_definition(self, full_name: str) -> dict: ...
    def _parent_store_compute(self): ...
    def _check_removed_columns(self, log: bool = ...) -> None: ...
    def _init_column(self, column_name: str) -> None: ...
    def _table_has_rows(self) -> int: ...
    def _auto_init(self): ...
    def init(self) -> None: ...
    def _check_parent_path(self) -> None: ...
    def _add_sql_constraints(self) -> None: ...
    def _add_inherited_fields(self) -> None: ...
    def _inherits_check(self) -> None: ...
    def _prepare_setup(self) -> None: ...
    def _setup_base(self) -> None: ...
    def _setup_fields(self) -> None: ...
    def _setup_complete(self) -> None: ...
    def fields_get(
        self, allfields: list[str] | None = ..., attributes: list[str] | None = ...
    ) -> dict[str, dict[str, Any]]: ...
    def check_field_access_rights(
        self, operation: str, field_names: Collection[str]
    ): ...
    def read(
        self, fields: Collection[str] | None = ..., load: str = ...
    ) -> list[dict[str, Any]]: ...
    def update_field_translations(
        self, field_name: str, translations: dict[str, Any]
    ) -> bool: ...
    def _update_field_translations(
        self,
        field_name: str,
        translations: dict[str, Any],
        digest: Callable | None = ...,
    ) -> bool: ...
    def get_field_translations(
        self, field_name: str, langs: list[str] | None = ...
    ) -> tuple[list[dict[str, Any]], dict[str, Any]]: ...
    def _get_base_lang(self) -> str: ...
    def _read_format(
        self, fnames: Collection[str], load: str = ...
    ) -> list[dict[str, Any]]: ...
    def _fetch_field(self, field: Field) -> None: ...
    def fetch(self, field_names: Collection[str]) -> None: ...
    def _determine_fields_to_fetch(
        self, field_names, ignore_when_in_cache: bool = ...
    ) -> list[Field]: ...
    def _fetch_query(
        self: _ModelT, query: Query, fields: Iterable[Field]
    ) -> _ModelT: ...
    def get_metadata(self) -> list[dict[str, Any]]: ...
    def get_base_url(self) -> str: ...
    def _check_company_domain(self, companies) -> list: ...
    def _check_company(self, fnames: Collection[str] | None = ...) -> None: ...
    def check_access_rights(
        self, operation: str, raise_exception: bool = ...
    ) -> bool: ...
    def check_access_rule(self, operation: str) -> None: ...
    def _filter_access_rules(self: _ModelT, operation: str) -> _ModelT: ...
    def _filter_access_rules_python(self, operation: str) -> _ModelT: ...
    def unlink(self): ...
    def write(self, vals: dict[str, Any]): ...
    def _write(self, vals: dict[str, Any]) -> None: ...
    @overload
    def create(self: _ModelT, vals_list: list[dict[str, Any]]) -> _ModelT: ...
    @overload
    def create(self: _ModelT, vals_list: dict[str, Any]) -> _ModelT: ...
    def _prepare_create_values(
        self, vals_list: list[dict[str, Any]]
    ) -> list[dict[str, Any]]: ...
    def _add_precomputed_values(self, vals_list: list[dict[str, Any]]) -> None: ...
    def _create(self: _ModelT, data_list: list[dict[str, Any]]) -> _ModelT: ...
    def _compute_field_value(self, field: Field) -> None: ...
    def _parent_store_create(self) -> None: ...
    def _parent_store_update_prepare(self: _ModelT, vals: dict) -> _ModelT: ...
    def _parent_store_update(self) -> None: ...
    def _load_records_write(self, values: dict[str, Any]) -> None: ...
    def _load_records_create(self, values: list[dict[str, Any]]): ...
    def _load_records(self, data_list: list[dict], update: bool = ...) -> BaseModel: ...
    def _where_calc(self, domain: list, active_test: bool = ...) -> Query: ...
    def _check_qorder(self, word: str) -> bool: ...
    def _apply_ir_rules(self, query: Query, mode: str = ...) -> None: ...
    def _order_to_sql(
        self, order: str, query: Query, alias: str | None = ..., reverse: bool = ...
    ) -> SQL: ...
    def _order_field_to_sql(
        self, alias: str, field_name: str, direction: SQL, nulls: SQL, query: Query
    ) -> SQL: ...
    def _flush_search(
        self,
        domain: list,
        fields: Sequence[str] | None = ...,
        order: str | None = ...,
        seen: set | None = ...,
    ) -> None: ...
    def _search(
        self: _ModelT,
        domain: list,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
        access_rights_uid: int | None = ...,
    ) -> Query: ...
    def _as_query(self, ordered: bool = ...) -> Query: ...
    def copy_data(
        self, default: dict[str, Any] | None = ...
    ) -> list[dict[str, Any]]: ...
    def copy_translations(
        self: _ModelT, new: _ModelT, excluded: Container[str] = ...
    ) -> None: ...
    def copy(self: _ModelT, default: dict[str, Any] | None = ...) -> _ModelT: ...
    def copy_multi(self: _ModelT, default: dict[str, Any] | None = ...) -> _ModelT: ...
    def exists(self: _ModelT) -> _ModelT: ...
    def _check_recursion(self, parent: str | None = ...) -> bool: ...
    def _check_m2m_recursion(self, field_name: str) -> bool: ...
    def _get_external_ids(self) -> dict[int, list[str]]: ...
    def get_external_id(self) -> dict[int, str]: ...
    @classmethod
    def is_transient(cls) -> bool: ...
    def search_read(
        self,
        domain: list | None = ...,
        fields: list[str] | None = ...,
        offset: int = ...,
        limit: int | None = ...,
        order: str | None = ...,
        **read_kwargs: str
    ) -> list[dict[str, Any]]: ...
    def toggle_active(self) -> None: ...
    def action_archive(self): ...
    def action_unarchive(self): ...
    def _register_hook(self) -> None: ...
    def _unregister_hook(self) -> None: ...
    def __init__(
        self, env: Environment, ids: tuple, prefetch_ids: Iterable[int]
    ) -> None: ...
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
    def with_user(self: _ModelT, user: Users | int) -> _ModelT: ...
    def with_company(self: _ModelT, company: Company | int) -> _ModelT: ...
    def with_context(self: _ModelT, *args, **kwargs) -> _ModelT: ...
    def with_prefetch(
        self: _ModelT, prefetch_ids: Iterable[int] | None = ...
    ) -> _ModelT: ...
    def _update_cache(self, values: dict[str, Any], validate: bool = ...): ...
    def _convert_to_record(self, values: dict[str, Any]): ...
    def _convert_to_write(self, values: dict[str, Any]) -> dict[str, Any]: ...
    def _mapped_func(self, func: Callable): ...
    @overload
    def mapped(self: _ModelT, func: Callable[[_ModelT], _Model2T]) -> _Model2T: ...
    @overload
    def mapped(self: _ModelT, func: Callable[[_ModelT], _T]) -> list[_T]: ...
    @overload
    def mapped(self, func: str) -> Any: ...
    @overload
    def filtered(self: _ModelT, func: Callable[[_ModelT], bool]) -> _ModelT: ...
    @overload
    def filtered(self: _ModelT, func: str) -> _ModelT: ...
    @overload
    def grouped(self: _ModelT, key: Callable[[_ModelT], _T]) -> dict[_T, _ModelT]: ...
    @overload
    def grouped(self: _ModelT, key: str) -> dict[Any, _ModelT]: ...
    def filtered_domain(self: _ModelT, domain: list) -> _ModelT: ...
    @overload
    def sorted(
        self: _ModelT, key: Callable[[_ModelT], Any] = ..., reverse: bool = ...
    ) -> _ModelT: ...
    @overload
    def sorted(
        self: _ModelT, key: str | None = ..., reverse: bool = ...
    ) -> _ModelT: ...
    def update(self, values: dict[str, Any]) -> None: ...
    def flush_model(self, fnames: Iterable[str] | None = ...) -> None: ...
    def flush_recordset(self, fnames: Iterable[str] | None = ...) -> None: ...
    def _flush(self, fnames: Iterable[str] | None = ...) -> None: ...
    def new(
        self: _ModelT,
        values: dict[str, Any] | None = ...,
        origin: _ModelT | None = ...,
        ref: Any | None = ...,
    ) -> _ModelT: ...
    @property
    def _origin(self: _ModelT) -> _ModelT: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self: _ModelT) -> Iterator[_ModelT]: ...
    def __reversed__(self) -> Iterator[_ModelT]: ...
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
    def __int__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    @overload
    def __getitem__(self: _ModelT, key: int | slice) -> _ModelT: ...
    @overload
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value): ...
    @property
    def _cache(self) -> RecordCache: ...
    def _in_cache_without(self: _ModelT, field: Field, limit: int = ...) -> _ModelT: ...
    def invalidate_model(
        self, fnames: Iterable[str] | None = ..., flush: bool = ...
    ) -> None: ...
    def invalidate_recordset(
        self, fnames: Iterable[str] | None = ..., flush: bool = ...
    ) -> None: ...
    def _invalidate_cache(
        self, fnames: Iterable[str] | None = ..., ids: Iterable[int] | None = ...
    ) -> None: ...
    def modified(
        self, fnames: Collection[str], create: bool = ..., before: bool = ...
    ) -> None: ...
    def _modified(
        self, fields: list, create: bool
    ) -> Iterator[tuple[Field, _ModelT, bool]]: ...
    def _modified_triggers(
        self: _ModelT, tree: TriggerTree, create: bool = ...
    ) -> Iterator[tuple[Field, _ModelT, bool]]: ...
    def _recompute_model(self, fnames: Iterable[str] | None = ...) -> None: ...
    def _recompute_recordset(self, fnames: Iterable[str] | None = ...) -> None: ...
    def _recompute_field(
        self, field: Field, ids: Iterable[int] | None = ...
    ) -> None: ...
    def _has_onchange(self, field: Field, other_fields: Container[Field]) -> bool: ...
    def _apply_onchange_methods(self, field_name: str, result: dict) -> None: ...
    def onchange(
        self,
        values: dict,
        field_names: list[str],
        fields_spec: dict,
    ) -> dict: ...
    def _get_placeholder_filename(self, field: str) -> str | bool: ...
    def _populate_factories(self) -> list[tuple[str, Callable[..., Iterator]]]: ...
    @property
    def _populate_sizes(self) -> dict[str, int]: ...
    @property
    def _populate_dependencies(self) -> list[str]: ...
    def _populate(self: _ModelT, size: str) -> _ModelT: ...

class RecordCache(MutableMapping):
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
