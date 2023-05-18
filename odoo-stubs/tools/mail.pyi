from email.message import Message
from re import Pattern
from typing import Any, FrozenSet, Literal

from lxml.etree import _Element
from lxml.html import clean
from markupsafe import Markup

tags_to_kill: list[str]
tags_to_remove: list[str]
allowed_tags: FrozenSet
safe_attrs: FrozenSet

class _Cleaner(clean.Cleaner):
    _style_re: Pattern
    _style_whitelist: list[str]
    strip_classes: bool
    sanitize_style: bool
    def __call__(self, doc: _Element) -> None: ...
    def tag_quote(self, el: _Element) -> None: ...
    def strip_class(self, el: _Element) -> None: ...
    def parse_style(self, el: _Element) -> None: ...

def html_sanitize(
    src: str,
    silent: bool = ...,
    sanitize_tags: bool = ...,
    sanitize_attributes: bool = ...,
    sanitize_style: bool = ...,
    sanitize_form: bool = ...,
    strip_style: bool = ...,
    strip_classes: bool = ...,
) -> Markup: ...

URL_REGEX: str
TEXT_URL_REGEX: str
HTML_TAG_URL_REGEX: str

def validate_url(url: str) -> str: ...
def is_html_empty(html_content: str) -> bool: ...
def html_keep_url(text: str) -> str: ...
def html2plaintext(
    html: str, body_id: str | None = ..., encoding: str = ...
) -> str: ...
def plaintext2html(text: str, container_tag: str = ...) -> Markup: ...
def append_content_to_html(
    html: str,
    content: str,
    plaintext: bool = ...,
    preserve: bool = ...,
    container_tag: str = ...,
) -> Markup: ...
def prepend_html_content(html_body: str, html_content: str) -> str: ...

email_re: Pattern
single_email_re: Pattern
mail_header_msgid_re: Pattern
email_addr_escapes_re: Pattern

def generate_tracking_message_id(res_id: str) -> str: ...
def email_send(
    email_from: str,
    email_to: str,
    subject: str,
    body: str,
    email_cc: str | None = ...,
    email_bcc: str | None = ...,
    reply_to: bool = ...,
    attachments: Any | None = ...,
    message_id: Any | None = ...,
    references: Any | None = ...,
    openobject_id: bool = ...,
    debug: bool = ...,
    subtype: str = ...,
    headers: Any | None = ...,
    smtp_server: Any | None = ...,
    smtp_port: Any | None = ...,
    ssl: bool = ...,
    smtp_user: Any | None = ...,
    smtp_password: Any | None = ...,
    cr: Any | None = ...,
    uid: Any | None = ...,
): ...
def email_split_tuples(text: str) -> list[str]: ...
def email_split(text: str) -> list[str]: ...
def email_split_and_format(text: str) -> list[str]: ...
def email_normalize(text: str) -> str | Literal[False]: ...
def email_escape_char(email_address: str) -> str: ...
def email_domain_extract(email: str) -> str | Literal[False]: ...
def decode_message_header(
    message: Message, header: str, separator: str = ...
) -> str: ...
def formataddr(pair: tuple[str, str], charset: str = ...) -> str: ...
def encapsulate_email(old_email: str, new_email: str) -> str: ...
