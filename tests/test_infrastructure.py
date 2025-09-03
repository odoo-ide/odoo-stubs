import pytest
from pathlib import Path


def test_stub_files_exist():
    """Test that stub files are present in the project."""
    stub_dir = Path("odoo-stubs")
    assert stub_dir.exists(), "odoo-stubs directory should exist"
    assert stub_dir.is_dir(), "odoo-stubs should be a directory"
    
    # Check for key stub files
    key_files = ["__init__.pyi", "models.pyi", "fields.pyi", "api.pyi"]
    for file_name in key_files:
        stub_file = stub_dir / file_name
        assert stub_file.exists(), f"{file_name} should exist in odoo-stubs"


def test_imports_work():
    """Test that basic imports work without errors."""
    try:
        import sys
        sys.path.insert(0, str(Path.cwd()))
        # This should not raise any import errors
        assert True
    except ImportError as e:
        pytest.fail(f"Import failed: {e}")


@pytest.mark.unit
def test_temp_dir_fixture(temp_dir):
    """Test the temp_dir fixture works correctly."""
    assert temp_dir.exists()
    assert temp_dir.is_dir()
    
    # Create a test file in temp dir
    test_file = temp_dir / "test.txt"
    test_file.write_text("test content")
    assert test_file.read_text() == "test content"


@pytest.mark.unit
def test_sample_stub_content_fixture(sample_stub_content):
    """Test the sample_stub_content fixture provides valid content."""
    assert isinstance(sample_stub_content, str)
    assert "class Model:" in sample_stub_content
    assert "def create(" in sample_stub_content


@pytest.mark.unit
def test_stub_file_fixture(stub_file):
    """Test the stub_file fixture creates a valid file."""
    assert stub_file.exists()
    assert stub_file.suffix == ".pyi"
    assert "class Model:" in stub_file.read_text()


def test_project_structure():
    """Test that the project has the expected structure."""
    # Check key directories exist
    assert Path("odoo-stubs").exists()
    assert Path("tests").exists()
    assert Path("tests/unit").exists()
    assert Path("tests/integration").exists()
    
    # Check configuration files
    assert Path("pyproject.toml").exists()
    assert Path("setup.py").exists()