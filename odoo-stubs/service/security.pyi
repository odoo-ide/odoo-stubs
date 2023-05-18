from typing import Literal

from ..api import Environment
from ..http import Session

def check(db: str, uid: int, passwd: str) -> None: ...
def compute_session_token(
    session: Session, env: Environment
) -> str | Literal[False]: ...
def check_session(session: Session, env: Environment) -> bool: ...
