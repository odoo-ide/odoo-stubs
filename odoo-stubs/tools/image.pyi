from typing import Any

def image_resize_image(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Any | None = ...,
    avoid_if_small: bool = ...,
): ...
def image_resize_and_sharpen(
    image, size, preserve_aspect_ratio: bool = ..., factor: float = ...
): ...
def image_save_for_web(image, fp: Any | None = ..., format: Any | None = ...): ...
def image_resize_image_big(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Any | None = ...,
    avoid_if_small: bool = ...,
): ...
def image_resize_image_medium(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Any | None = ...,
    avoid_if_small: bool = ...,
): ...
def image_resize_image_small(
    base64_source,
    size=...,
    encoding: str = ...,
    filetype: Any | None = ...,
    avoid_if_small: bool = ...,
): ...
def crop_image(
    data,
    type: str = ...,
    ratio: bool = ...,
    thumbnail_ratio: Any | None = ...,
    image_format: str = ...,
): ...
def image_colorize(original, randomize: bool = ..., color=...): ...
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
): ...
def image_resize_images(
    vals, big_name: str = ..., medium_name: str = ..., small_name: str = ...
) -> None: ...
