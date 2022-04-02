from click.testing import CliRunner
from challenge.main import main


def test_main_stdin():
    runner = CliRunner()
    result = runner.invoke(main, args="-", input='Now is the time for all good people')
    assert not result.exception
    assert result.output == 'Now is the time for all good people\n'
