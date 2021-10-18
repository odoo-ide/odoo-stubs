from typing import Any

JSON_SCRIPTSAFE_MAPPER: Any

class _ScriptSafe(str):
    def __html__(self): ...

class JSON:
    def loads(self, *args, **kwargs): ...
    def dumps(self, *args, **kwargs): ...

scriptsafe: Any
