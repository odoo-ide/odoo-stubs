from typing import Any, Iterable

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import ArrayObject as ArrayObject
from PyPDF2.utils import b_ as b_

DEFAULT_PDF_DATETIME_FORMAT: str

def merge_pdf(pdf_data: Iterable[bytes]) -> bytes: ...

class OdooPdfFileWriter(PdfFileWriter):
    def __init__(self, *args, **kwargs):
        None
    def addAttachment(self, fname: str, fdata, subtype: str = ...) -> None: ...
    def cloneReaderDocumentRoot(self, reader: PdfFileReader) -> None: ...
    def convert_to_pdfa(self) -> None: ...
    def add_file_metadata(self, metadata_content: bytes) -> None: ...
