from typing import *

from . import api, fields
from .modules.registry import Registry


class MetaModel(api.Meta):
    module_to_models: Any = ...

    def __init__(self, name: Any, bases: Any, attrs: Any) -> None: ...


class BaseModel(MetaModel('DummyModel', (object,), {'_register': False})):
    _id: int
    _ids: List[int]
    _fields: Dict[str, fields.Field]
    _inherit_children: Set[str]
    pool: Registry
    env: api.Environment

    __bases__: Tuple[BaseModel, ...]
    def __iter__(self) -> BaseModel: ...

    def browse(self, ids: Optional[Union[Iterable[int], int]]) -> BaseModel: ...
    def search(self, args: List, offset: Optional[int] = 0, limit=Optional[int], order=Optional[str], count=Optional[int]) -> BaseModel: ...


AbstractModel = BaseModel


class Model(AbstractModel): ...


class TransientModel(Model): ...
