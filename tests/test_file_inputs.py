from click.testing import CliRunner
from main import main


def test_main_stdin():
    runner = CliRunner()
    result = runner.invoke(main, args="-", input='Now is the time for all good people')
    assert not result.exception
    assert result.output.find('all good people') > 1


def test_main_filename():
    runner = CliRunner()
    result = runner.invoke(main, args="text/test1.txt")
    assert not result.exception
    assert result.output.find('all good people') > 1
