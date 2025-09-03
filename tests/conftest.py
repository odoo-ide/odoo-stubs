import pytest
import tempfile
import shutil
from pathlib import Path
from typing import Generator


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Provide a temporary directory that gets cleaned up after test."""
    temp_path = Path(tempfile.mkdtemp())
    try:
        yield temp_path
    finally:
        shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def sample_stub_content():
    """Provide sample stub file content for testing."""
    return '''
from typing import Any, Optional

class Model:
    def __init__(self) -> None: ...
    def create(self, vals: dict[str, Any]) -> "Model": ...
    def search(self, domain: list[tuple[str, str, Any]]) -> "Model": ...
    def write(self, vals: dict[str, Any]) -> bool: ...
    def unlink(self) -> bool: ...

def browse(self, ids: list[int]) -> "Model": ...
'''.strip()


@pytest.fixture
def mock_odoo_env(monkeypatch):
    """Mock basic Odoo environment for testing."""
    class MockEnv:
        def __init__(self):
            self.cr = MockCursor()
            self.uid = 1
            self.context = {}
        
        def __getitem__(self, model_name):
            return MockModel(model_name)
    
    class MockCursor:
        def execute(self, query, params=None):
            pass
        
        def fetchall(self):
            return []
        
        def fetchone(self):
            return None
    
    class MockModel:
        def __init__(self, name):
            self._name = name
        
        def create(self, vals):
            return self
        
        def search(self, domain):
            return self
        
        def browse(self, ids):
            return self
    
    mock_env = MockEnv()
    monkeypatch.setattr("odoo.api.Environment", lambda: mock_env)
    return mock_env


@pytest.fixture
def stub_file(temp_dir, sample_stub_content):
    """Create a temporary stub file for testing."""
    stub_file = temp_dir / "test_model.pyi"
    stub_file.write_text(sample_stub_content)
    return stub_file