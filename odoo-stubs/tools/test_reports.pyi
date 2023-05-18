from typing import Any, Literal

from ..sql_db import Cursor
from . import config as config

def try_report(
    cr: Cursor,
    uid: int,
    rname: str,
    ids,
    data: Any | None = ...,
    context: dict | None = ...,
    our_module: Any | None = ...,
    report_type: Any | None = ...,
) -> bool: ...
def try_report_action(
    cr: Cursor,
    uid: int,
    action_id: int,
    active_model: str | None = ...,
    active_ids: list[int] | None = ...,
    wiz_data: dict | None = ...,
    wiz_buttons: list[str] | None = ...,
    context: dict | None = ...,
    our_module: str | None = ...,
) -> Literal[True]: ...
