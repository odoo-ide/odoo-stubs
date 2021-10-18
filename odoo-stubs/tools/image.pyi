from PIL import IcoImagePlugin as IcoImagePlugin, ImageOps as ImageOps
from typing import Any

FILETYPE_BASE64_MAGICWORD: Any
EXIF_TAG_ORIENTATION: int
EXIF_TAG_ORIENTATION_TO_TRANSPOSE_METHODS: Any
IMAGE_MAX_RESOLUTION: float

class ImageProcess:
    base64_source: Any
    operationsCount: int
    image: bool
    original_format: Any
    def __init__(self, base64_source, verify_resolution: bool = ...) -> None: ...
    def image_base64(self, quality: int = ..., output_format: str = ...): ...
    def resize(self, max_width: int = ..., max_height: int = ...): ...
    def crop_resize(self, max_width, max_height, center_x: float = ..., center_y: float = ...): ...
    def colorize(self): ...

def image_process(base64_source, size=..., verify_resolution: bool = ..., quality: int = ..., crop: Any | None = ..., colorize: bool = ..., output_format: str = ...): ...
def average_dominant_color(colors, mitigate: int = ..., max_margin: int = ...): ...
def image_fix_orientation(image): ...
def base64_to_image(base64_source): ...
def image_to_base64(image, format, **params): ...
def is_image_size_above(base64_source_1, base64_source_2): ...
def image_guess_size_from_field_name(field_name): ...
def image_data_uri(base64_source): ...
def get_saturation(rgb): ...
def get_lightness(rgb): ...
def hex_to_rgb(hx): ...
def rgb_to_hex(rgb): ...
