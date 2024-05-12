from contextlib import contextmanager
from typing import Iterator

from ....models import AbstractModel
from ..core import WorkContext

class Collection(AbstractModel):
    @contextmanager
    def work_on(self, model_name: str, **kwargs) -> Iterator[WorkContext]: ...
