from pcmd import __version__
from typer.testing import CliRunner
from pcmd.main import app, f_reader_err
from pcmd.main import get_commands, f_remove, f_add, f_syntax_err, f_empty

runner = CliRunner()


def test_version():
    assert __version__ == '2.0.0'


def test_get_commands_1():
    assert type(get_commands()).__name__ == "dict"


def test_get_commands_2():
    assert get_commands()['dir'] == "dir"


def test_get_commands_3():
    try:
        a = get_commands()['test-3']
    except KeyError:
        a = None
    assert a is None


def test_get_commands_4():
    assert type(get_commands()['check']).__name__ == "list"


def test_app_dynamic():
    commands = get_commands()  # gets the commands
    result = runner.invoke(app, ["run", "main-hi"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["run", "main-chain"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["run", "main-unknown"])
    assert result.exit_code == 0
    f_remove()  # removes the file for testing purposes
    result = runner.invoke(app, ["run", "main-unknown"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["inspect"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    f_remove()
    f_syntax_err()
    result = runner.invoke(app, ["inspect"])
    assert result.exit_code == 0
    f_remove()
    f_reader_err()
    result = runner.invoke(app, ["inspect"])
    assert result.exit_code == 0
    f_remove()
    f_empty()
    result = runner.invoke(app, ["inspect"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["init", "-f"])
    assert result.exit_code == 0
    f_add(commands)  # adds the file back


def test_app_init():
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 0
    assert "'cmd.yaml' already exists." in result.stdout


def test_app_inspect():
    result = runner.invoke(app, ["inspect"])
    assert result.exit_code == 0
    assert "PCMD Inspection : " in result.stdout
    assert "\t'cmd.yaml' file found!" in result.stdout
    assert "\t'cmd.yaml' is valid!" in result.stdout


def test_app_list():
    commands = get_commands()  # gets the commands
    result = runner.invoke(app, ["list", "-p"])
    assert result.exit_code == 0
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    f_remove()
    f_empty()
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    f_add(commands)  # adds the file back


def test_app_fish():
    result = runner.invoke(app, ["fish"], input="n\n")
    assert result.exit_code == 0
