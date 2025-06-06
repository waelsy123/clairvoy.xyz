import pathlib

README_PATH = pathlib.Path(__file__).resolve().parents[1] / "README.md"

def test_codex_section_present():
    text = README_PATH.read_text()
    assert "## Codex Usage" in text
    assert "prompts/" in text
    assert "EIPs/" in text
