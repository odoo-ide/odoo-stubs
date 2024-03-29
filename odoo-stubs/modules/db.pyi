from enum import IntEnum

from ..sql_db import Cursor

def is_initialized(cr: Cursor) -> bool: ...
def initialize(cr: Cursor) -> None: ...
def create_categories(cr: Cursor, categories: list[str]) -> int | None: ...

class FunctionStatus(IntEnum):
    MISSING: int
    PRESENT: int
    INDEXABLE: int

def has_unaccent(cr: Cursor) -> bool: ...
def has_trigram(cr: Cursor) -> bool: ...
