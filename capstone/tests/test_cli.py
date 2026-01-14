import pytest
from src.cli import CLIHandler

def test_cli_load_success(valid_config):
    handler = CLIHandler(config_path=valid_config)
    assert handler.defaults['files_count'] == '2'

def test_cli_parsing(valid_config, monkeypatch):
    monkeypatch.setattr("sys.argv", ["magicgenerator", "--files_count", "5"])
    handler = CLIHandler(config_path=valid_config)
    args = handler.parse()
    assert args.files_count == 5
    assert args.file_name == "test"

def test_missing_section_exits(tmp_path):
    cfg = tmp_path / "wrong.ini"
    cfg.write_text("[WRONG_SECTION]\nkey=val")
    with pytest.raises(SystemExit):
        CLIHandler(config_path=str(cfg))
