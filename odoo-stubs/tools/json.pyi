JSON_SCRIPTSAFE_MAPPER: dict[str, str]

class JSON:
    def loads(self, *args, **kwargs): ...
    def dumps(self, *args, **kwargs) -> str: ...

scriptsafe: JSON
