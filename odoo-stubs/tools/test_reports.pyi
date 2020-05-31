from . import config as config
from typing import Any, Optional

_logger: Any
_test_logger: Any

def try_report(cr: Any, uid: Any, rname: Any, ids: Any, data: Optional[Any] = ..., context: Optional[Any] = ..., our_module: Optional[Any] = ..., report_type: Optional[Any] = ...): ...
def try_report_action(cr: Any, uid: Any, action_id: Any, active_model: Optional[Any] = ..., active_ids: Optional[Any] = ..., wiz_data: Optional[Any] = ..., wiz_buttons: Optional[Any] = ..., context: Optional[Any] = ..., our_module: Optional[Any] = ...): ...
