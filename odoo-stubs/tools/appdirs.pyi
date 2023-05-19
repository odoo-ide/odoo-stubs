__version_info__: tuple

def user_data_dir(
    appname: str | None = ...,
    appauthor: str | None = ...,
    version: str | None = ...,
    roaming: bool = ...,
) -> str: ...
def site_data_dir(
    appname: str | None = ...,
    appauthor: str | None = ...,
    version: str | None = ...,
    multipath: bool = ...,
) -> str: ...
def user_config_dir(
    appname: str | None = ...,
    appauthor: str | None = ...,
    version: str | None = ...,
    roaming: bool = ...,
) -> str: ...
def site_config_dir(
    appname: str | None = ...,
    appauthor: str | None = ...,
    version: str | None = ...,
    multipath: bool = ...,
) -> str: ...
def user_cache_dir(
    appname: str | None = ...,
    appauthor: str | None = ...,
    version: str | None = ...,
    opinion: bool = ...,
) -> str: ...
def user_log_dir(
    appname: str | None = ...,
    appauthor: str | None = ...,
    version: str | None = ...,
    opinion: bool = ...,
) -> str: ...

class AppDirs:
    appname: str
    appauthor: str | None
    version: str | None
    roaming: bool
    multipath: bool
    def __init__(
        self,
        appname: str,
        appauthor: str | None = ...,
        version: str | None = ...,
        roaming: bool = ...,
        multipath: bool = ...,
    ) -> None: ...
    @property
    def user_data_dir(self) -> str: ...
    @property
    def site_data_dir(self) -> str: ...
    @property
    def user_config_dir(self) -> str: ...
    @property
    def site_config_dir(self) -> str: ...
    @property
    def user_cache_dir(self) -> str: ...
    @property
    def user_log_dir(self) -> str: ...
