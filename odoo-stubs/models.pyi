from typing import Any

from . import api


class MetaModel(api.Meta):
    module_to_models: Any = ...

    def __init__(self, name: Any, bases: Any, attrs: Any) -> None: ...


class BaseModel(MetaModel('DummyModel', (object,), {'_register': False})):
    _ids: list
    def __iter__(self) -> BaseModel: ...
    def _browse(self) -> BaseModel: ...


AbstractModel = BaseModel


class Model(AbstractModel): ...


class TransientModel(Model): ...
