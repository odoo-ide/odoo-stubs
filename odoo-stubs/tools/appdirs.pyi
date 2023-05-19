from typing import Any

__version_info__: Any

def user_data_dir(
    appname: Any | None = ...,
    appauthor: Any | None = ...,
    version: Any | None = ...,
    roaming: bool = ...,
): ...
def site_data_dir(
    appname: Any | None = ...,
    appauthor: Any | None = ...,
    version: Any | None = ...,
    multipath: bool = ...,
): ...
def user_config_dir(
    appname: Any | None = ...,
    appauthor: Any | None = ...,
    version: Any | None = ...,
    roaming: bool = ...,
): ...
def site_config_dir(
    appname: Any | None = ...,
    appauthor: Any | None = ...,
    version: Any | None = ...,
    multipath: bool = ...,
): ...
def user_cache_dir(
    appname: Any | None = ...,
    appauthor: Any | None = ...,
    version: Any | None = ...,
    opinion: bool = ...,
): ...
def user_log_dir(
    appname: Any | None = ...,
    appauthor: Any | None = ...,
    version: Any | None = ...,
    opinion: bool = ...,
): ...

class AppDirs:
    appname: Any
    appauthor: Any
    version: Any
    roaming: Any
    multipath: Any
    def __init__(
        self,
        appname,
        appauthor: Any | None = ...,
        version: Any | None = ...,
        roaming: bool = ...,
        multipath: bool = ...,
    ) -> None: ...
    @property
    def user_data_dir(self): ...
    @property
    def site_data_dir(self): ...
    @property
    def user_config_dir(self): ...
    @property
    def site_config_dir(self): ...
    @property
    def user_cache_dir(self): ...
    @property
    def user_log_dir(self): ...
