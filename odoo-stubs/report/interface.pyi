from typing import Any

def toxml(value): ...

class report_int:
    _reports: Any
    __name: Any
    name: Any
    id: int
    name2: Any
    title: Any
    def __init__(self, name, register: bool = ...) -> None: ...
    def create(self, cr, uid, ids, datas, context: Any | None = ...): ...

class report_rml(report_int):
    table: Any
    internal_header: bool
    tmpl: Any
    xsl: Any
    bin_datas: Any
    generators: Any
    def __init__(self, name, table, tmpl, xsl, register: bool = ...) -> None: ...
    title: Any
    def create(self, cr, uid, ids, datas, context: Any | None = ...): ...
    def create_xml(self, cr, uid, ids, datas, context: Any | None = ...): ...
    def post_process_xml_data(self, cr, uid, xml, context: Any | None = ...): ...
    def create_rml(self, cr, xml, uid, context: Any | None = ...): ...
    def create_pdf(
        self,
        rml,
        localcontext: Any | None = ...,
        logo: Any | None = ...,
        title: Any | None = ...,
    ): ...
    def create_html(
        self,
        rml,
        localcontext: Any | None = ...,
        logo: Any | None = ...,
        title: Any | None = ...,
    ): ...
    def create_txt(
        self, rml, localcontext, logo: Any | None = ..., title: Any | None = ...
    ): ...
    def create_html2html(
        self,
        rml,
        localcontext: Any | None = ...,
        logo: Any | None = ...,
        title: Any | None = ...,
    ): ...
    def create_raw(
        self,
        rml,
        localcontext: Any | None = ...,
        logo: Any | None = ...,
        title: Any | None = ...,
    ): ...
    def create_sxw(self, rml, localcontext: Any | None = ...): ...
    def create_odt(self, rml, localcontext: Any | None = ...): ...
    def create_makohtml2html(self, html, localcontext: Any | None = ...): ...
    def _get_path(self): ...
