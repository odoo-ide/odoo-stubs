from unittest import BaseTestSuite

class TestSuite(BaseTestSuite):
    def run(self, result, debug: bool = ...): ...

class OdooSuite(TestSuite):
    def has_http_case(self) -> bool: ...
