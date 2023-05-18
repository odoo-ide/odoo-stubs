from typing import Any, Optional

FILETYPE_BASE64_MAGICWORD: Any

def image_resize_image(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Optional[Any] = ...,
    avoid_if_small: bool = ...,
    upper_limit: bool = ...,
): ...
def image_resize_and_sharpen(
    image,
    size,
    preserve_aspect_ratio: bool = ...,
    factor: float = ...,
    upper_limit: bool = ...,
): ...
def image_save_for_web(image, fp: Optional[Any] = ..., format: Optional[Any] = ...): ...
def image_resize_image_big(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Optional[Any] = ...,
    avoid_if_small: bool = ...,
): ...
def image_resize_image_medium(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Optional[Any] = ...,
    avoid_if_small: bool = ...,
): ...
def image_resize_image_small(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Optional[Any] = ...,
    avoid_if_small: bool = ...,
): ...
def crop_image(
    data,
    type: str = ...,
    ratio: bool = ...,
    size: Optional[Any] = ...,
    image_format: Optional[Any] = ...,
): ...
def image_colorize(original, randomize: bool = ..., color: Any = ...): ...
def image_get_resized_images(
    base64_source,
    return_big: bool = ...,
    return_medium: bool = ...,
    return_small: bool = ...,
    big_name: str = ...,
    medium_name: str = ...,
    small_name: str = ...,
    avoid_resize_big: bool = ...,
    avoid_resize_medium: bool = ...,
    avoid_resize_small: bool = ...,
    sizes: Any = ...,
): ...
def image_resize_images(
    vals,
    big_name: str = ...,
    medium_name: str = ...,
    small_name: str = ...,
    sizes: Any = ...,
) -> None: ...
def image_data_uri(base64_source): ...
