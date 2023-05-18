from typing import Any, Optional

from . import config as config

_logger: Any
_test_logger: Any

def try_report(
    cr,
    uid,
    rname,
    ids,
    data: Optional[Any] = ...,
    context: Optional[Any] = ...,
    our_module: Optional[Any] = ...,
    report_type: Optional[Any] = ...,
): ...
def try_report_action(
    cr,
    uid,
    action_id,
    active_model: Optional[Any] = ...,
    active_ids: Optional[Any] = ...,
    wiz_data: Optional[Any] = ...,
    wiz_buttons: Optional[Any] = ...,
    context: Optional[Any] = ...,
    our_module: Optional[Any] = ...,
): ...
