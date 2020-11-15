from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import ArrayObject as ArrayObject
from PyPDF2.utils import b_ as b_
from typing import Any, Optional

DEFAULT_PDF_DATETIME_FORMAT: str

def _unwrapping_get(self, key: Any, default: Optional[Any] = ...): ...

class BrandedFileWriter(PdfFileWriter):
    def __init__(self) -> None: ...
PdfFileWriter = BrandedFileWriter

def merge_pdf(pdf_data: Any): ...
def rotate_pdf(pdf: Any): ...

old_init: Any

class OdooPdfFileReader(PdfFileReader):
    def getAttachments(self): ...

class OdooPdfFileWriter(PdfFileWriter):
    def _create_attachment_object(self, attachment: Any): ...
    def addAttachment(self, fname: Any, fdata: Any) -> None: ...
