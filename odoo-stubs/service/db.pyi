from functools import wraps as wraps
from typing import Any, Optional

class DatabaseExists(Warning): ...

def check_db_management_enabled(method): ...
def check_super(passwd): ...
def exp_create_database(
    db_name,
    demo,
    lang,
    user_password: str = ...,
    login: str = ...,
    country_code: Optional[Any] = ...,
): ...
def exp_duplicate_database(db_original_name, db_name): ...
def exp_drop(db_name): ...
def exp_dump(db_name, format): ...
def dump_db_manifest(cr): ...
def dump_db(db_name, stream, backup_format: str = ...): ...
def exp_restore(db_name, data, copy: bool = ...): ...
def restore_db(db, dump_file, copy: bool = ...) -> None: ...
def exp_rename(old_name, new_name): ...
def exp_change_admin_password(new_password): ...
def exp_migrate_databases(databases): ...
def exp_db_exist(db_name): ...
def list_dbs(force: bool = ...): ...
def list_db_incompatible(databases): ...
def exp_list(document: bool = ...): ...
def exp_list_lang(): ...
def exp_list_countries(): ...
def exp_server_version(): ...
def dispatch(method, params): ...
