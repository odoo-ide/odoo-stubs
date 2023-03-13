from re import Pattern

class TagsSelector:
    filter_spec_re: Pattern
    exclude: set
    include: set
    def __init__(self, spec: str) -> None: ...
    def check(self, test) -> bool: ...
