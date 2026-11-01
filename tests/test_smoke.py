from typer.testing import CliRunner

import angio
from angio.cli import app


def test_version_is_set() -> None:
    assert angio.__version__


def test_cli_version() -> None:
    result = CliRunner().invoke(app, ["version"])
    assert result.exit_code == 0
    assert angio.__version__ in result.output