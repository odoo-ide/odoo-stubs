from typing import Iterable

from ...models import AbstractModel
from .core import DEFAULT_CACHE_SIZE as DEFAULT_CACHE_SIZE
from .core import ComponentRegistry as ComponentRegistry

class ComponentBuilder(AbstractModel):
    def build_registry(
        self,
        components_registry: ComponentRegistry,
        states: Iterable[str] | None = None,
        exclude_addons: Iterable[str] | None = None,
    ) -> None: ...
    def load_components(
        self, module: str, components_registry: ComponentRegistry | None = None
    ) -> None: ...
