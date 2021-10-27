from typing import Any

class Session:
    cr: Any
    uid: Any
    def __init__(self, cr, uid) -> None: ...

class Record:
    model: Any
    id: Any
    def __init__(self, model, record_id) -> None: ...

class WorkflowActivity:
    KIND_FUNCTION: str
    KIND_DUMMY: str
    KIND_STOPALL: str
    KIND_SUBFLOW: str
