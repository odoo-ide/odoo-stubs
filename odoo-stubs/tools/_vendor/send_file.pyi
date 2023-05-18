from datetime import datetime
from os import PathLike
from typing import IO, Callable

from werkzeug import Response

def send_file(
    path_or_file: PathLike | str | IO[bytes],
    environ: dict,
    mimetype: str | None = ...,
    as_attachment: bool = ...,
    download_name: str | None = ...,
    conditional: bool = ...,
    etag: bool | str = ...,
    last_modified: datetime | int | float | None = ...,
    max_age: int | Callable[[str | None], int | None] | None = ...,
    use_x_sendfile: bool = ...,
    response_class: type[Response] = ...,
    _root_path: PathLike | str | None = ...,
) -> Response: ...
