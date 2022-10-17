from markupsafe import Markup

JSON_SCRIPTSAFE_MAPPER: dict[str, str]

class _ScriptSafe(str):
    def __html__(self) -> Markup: ...

class JSON:
    def loads(self, *args, **kwargs): ...
    def dumps(self, *args, **kwargs) -> _ScriptSafe: ...

scriptsafe: JSON
