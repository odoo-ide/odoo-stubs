from typing import Any

to_19_fr: Any
tens_fr: Any
denom_fr: Any

def french_number(val): ...
def amount_to_text_fr(number, currency): ...

to_19_nl: Any
tens_nl: Any
denom_nl: Any

def dutch_number(val): ...
def amount_to_text_nl(number, currency): ...
def add_amount_to_text_function(lang, func) -> None: ...
def amount_to_text(nbr, lang: str = ..., currency: str = ...): ...