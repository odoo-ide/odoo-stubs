from typing import Any, Optional

__version_info__: Any
__version__: Any

def user_data_dir(
    appname: Optional[Any] = ...,
    appauthor: Optional[Any] = ...,
    version: Optional[Any] = ...,
    roaming: bool = ...,
): ...
def site_data_dir(
    appname: Optional[Any] = ...,
    appauthor: Optional[Any] = ...,
    version: Optional[Any] = ...,
    multipath: bool = ...,
): ...
def user_config_dir(
    appname: Optional[Any] = ...,
    appauthor: Optional[Any] = ...,
    version: Optional[Any] = ...,
    roaming: bool = ...,
): ...
def site_config_dir(
    appname: Optional[Any] = ...,
    appauthor: Optional[Any] = ...,
    version: Optional[Any] = ...,
    multipath: bool = ...,
): ...
def user_cache_dir(
    appname: Optional[Any] = ...,
    appauthor: Optional[Any] = ...,
    version: Optional[Any] = ...,
    opinion: bool = ...,
): ...
def user_log_dir(
    appname: Optional[Any] = ...,
    appauthor: Optional[Any] = ...,
    version: Optional[Any] = ...,
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
        appauthor: Optional[Any] = ...,
        version: Optional[Any] = ...,
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

def _get_win_folder_from_registry(csidl_name): ...
def _get_win_folder_with_pywin32(csidl_name): ...
def _get_win_folder_with_ctypes(csidl_name): ...
