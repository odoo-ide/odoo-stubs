from typing import Any

class Query:
    tables: Any
    where_clause: Any
    where_clause_params: Any
    joins: Any
    extras: Any
    def __init__(
        self,
        tables: Any | None = ...,
        where_clause: Any | None = ...,
        where_clause_params: Any | None = ...,
        joins: Any | None = ...,
        extras: Any | None = ...,
    ) -> None: ...
    def add_join(
        self,
        connection,
        implicit: bool = ...,
        outer: bool = ...,
        extra: Any | None = ...,
        extra_params=...,
    ): ...
    def get_sql(self): ...
