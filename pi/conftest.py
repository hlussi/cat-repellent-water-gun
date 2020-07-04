import pytest
import os


def pytest_logger_config(logger_config):
    logger_config.add_loggers(['testrun', 'setup'], stdout_level='debug')
    logger_config.set_log_option_default('testrun,setup')


def pytest_addoption(parser):
    parser.addoption(
        "--config_file", action="store", default="",
        help="The relative path to a config file which uses the same format as the default one."
    )

@pytest.fixture(scope='module')
def config_file(request):
    config_file_path = request.config.getoption("--config_file")
    try:
        open(config_file_path, 'r')
    except FileNotFoundError:
        if config_file_path == '':
            pytest.exit(f"Error: No config file was specified (Option: --config_file=<your-config-file>).")
        pytest.exit(f"Error: File \'{config_file_path}\' not found.")
    return config_file_path
