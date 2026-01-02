import pytest

@pytest.fixture
def valid_config(tmp_path):
    cfg = tmp_path / "config.ini"
    content = (
        "[AppConfig]\n"
        "path_to_save_files = ./test_out\n"
        "files_count = 2\n"
        "file_name = test\n"
        "file_prefix = count\n"
        "data_schema = {}\n"
        "data_lines = 10\n"
        "clear_path = False\n"
        "multiprocessing = 1\n"
    )
    cfg.write_text(content)
    return str(cfg)
