from typing import Any, Optional

tags_to_kill: Any
tags_to_remove: Any
allowed_tags: Any
safe_attrs: Any

def html_sanitize(
    src,
    silent: bool = ...,
    sanitize_tags: bool = ...,
    sanitize_attributes: bool = ...,
    sanitize_style: bool = ...,
    strip_style: bool = ...,
    strip_classes: bool = ...,
): ...
def html_keep_url(text): ...
def html2plaintext(html, body_id: Optional[Any] = ..., encoding: str = ...): ...
def plaintext2html(text, container_tag: bool = ...): ...
def append_content_to_html(
    html,
    content,
    plaintext: bool = ...,
    preserve: bool = ...,
    container_tag: bool = ...,
): ...

email_re: Any
single_email_re: Any
command_re: Any
reference_re: Any
discussion_re: Any
mail_header_msgid_re: Any
email_addr_escapes_re: Any

def generate_tracking_message_id(res_id): ...
def email_send(
    email_from,
    email_to,
    subject,
    body,
    email_cc: Optional[Any] = ...,
    email_bcc: Optional[Any] = ...,
    reply_to: bool = ...,
    attachments: Optional[Any] = ...,
    message_id: Optional[Any] = ...,
    references: Optional[Any] = ...,
    openobject_id: bool = ...,
    debug: bool = ...,
    subtype: str = ...,
    headers: Optional[Any] = ...,
    smtp_server: Optional[Any] = ...,
    smtp_port: Optional[Any] = ...,
    ssl: bool = ...,
    smtp_user: Optional[Any] = ...,
    smtp_password: Optional[Any] = ...,
    cr: Optional[Any] = ...,
    uid: Optional[Any] = ...,
): ...
def email_split(text): ...
def email_split_and_format(text): ...
def email_references(references): ...
def decode_smtp_header(smtp_header): ...
def decode_message_header(message, header, separator: str = ...): ...
def formataddr(pair, charset: str = ...): ...
