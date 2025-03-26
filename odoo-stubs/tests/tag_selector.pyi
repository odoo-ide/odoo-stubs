from re import Pattern

from ..tools import OrderedSet

class TagsSelector:
    filter_spec_re: Pattern
    exclude: set
    include: set
    parameters: OrderedSet
    def __init__(self, spec: str) -> None: ...
    def check(self, test) -> bool: ...
