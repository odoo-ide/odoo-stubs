from typing import Any

import lxml.html.clean as clean

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
def html2plaintext(html, body_id: Any | None = ..., encoding: str = ...): ...
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

def generate_tracking_message_id(res_id): ...
def email_send(
    email_from,
    email_to,
    subject,
    body,
    email_cc: Any | None = ...,
    email_bcc: Any | None = ...,
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
def email_split(text): ...
def email_split_and_format(text): ...
def email_references(references): ...
def decode_smtp_header(smtp_header): ...
def decode_message_header(message, header, separator: str = ...): ...
