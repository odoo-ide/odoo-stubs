from typing import Any, Optional

from ..exceptions import except_orm as except_orm
from ..models import LOG_ACCESS_COLUMNS as LOG_ACCESS_COLUMNS
from ..models import MAGIC_COLUMNS as MAGIC_COLUMNS
from ..models import AbstractModel as AbstractModel
from ..models import BaseModel
from ..models import MetaModel as MetaModel
from ..models import Model as Model
from ..models import TransientModel as TransientModel

browse_record_list = BaseModel

class BRM(type):
    def __instancecheck__(self, inst): ...

browse_record: Any

class NBM(type):
    def __instancecheck__(self, inst): ...

browse_null: Any

def transfer_field_to_modifiers(field, modifiers) -> None: ...
def transfer_node_to_modifiers(
    node, modifiers, context: Optional[Any] = ..., in_tree_view: bool = ...
) -> None: ...
def simplify_modifiers(modifiers) -> None: ...
def transfer_modifiers_to_node(modifiers, node) -> None: ...
def setup_modifiers(
    node,
    field: Optional[Any] = ...,
    context: Optional[Any] = ...,
    in_tree_view: bool = ...,
) -> None: ...
def test_modifiers(what, expected) -> None: ...
def modifiers_tests() -> None: ...
