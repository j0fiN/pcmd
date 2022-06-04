"""
    main
    ~~~~~~~
    Command functions of the pcmd CLI.

    FUNCTIONS
    ~~~~~~~
    callback
    run
    list
    inspect
    init
    fish
    add
"""
from typing import Any, List, Optional, Tuple
import yaml  # type: ignore
import typer
import os
from .__init__ import __version__  # type: ignore
from .__core__ import (
    get_commands,
    prettier, save_cmd_yaml,
    add_load_and_save_echo,
    run_command,
    echo_cmd_not_found
)
from .__echoes__ import (
    echo_file_created,
    echo_file_empty,
    echo_file_error,
    echo_file_exist,
    echo_file_found,
    echo_file_not_found,
    echo_file_valid,
    echo_cmd_changed,
    echo_info_del_init,
    echo_info_init,
    echo_list_header,
    echo_inspect_header,
    echo_fish
)
from .__const__ import EGG, URLS, EXCEPTIONS
app = typer.Typer()


@app.callback()
def callback() -> None:
    """
    PCMD\n
    A super simple terminal command shortener\n
    Version : v2.2.0\n
    """


@app.command()
def run(command: str, args: Optional[List[str]] = typer.Option(None, "--args", "-a")) -> None:
    """
    Run terminal command / runs multiple command chains.\n
    Check docs for warnings (pcmd fish for link).
    
    """
    commands = get_commands()
    if commands is None:
        echo_file_not_found()
    else:
        try:
            cmds = commands[command]
            if type(cmds).__name__ == 'list':
                for cmd in cmds:
                    run_command(cmd, args)
            else:
                run_command(cmds, args)
        except KeyError:
            echo_cmd_not_found(command)


@app.command()
def list(
    pretty: bool = typer.Option(False, "--pretty", "-p")
) -> None:
    """
    Outputs the complete cmd.yaml (use -p for pretty).
    """
    commands = get_commands()
    if commands is None:
        echo_file_not_found()
    else:
        echo_list_header()
        if commands == {}:
            echo_file_empty()
        else:
            if pretty:
                prettier(commands)
            else:
                typer.echo(yaml.dump(commands, indent=2,
                                     explicit_start=True,
                                     explicit_end=True))


@app.command()
def inspect() -> None:
    """
    Checks if cmd.yaml exists and validates it.
    """
    echo_inspect_header()
    if os.path.exists('cmd.yaml'):
        echo_file_found()
        try:
            with open('cmd.yaml', 'r') as f:
                data = yaml.load(f, Loader=yaml.BaseLoader)
                if data is not None:
                    echo_file_valid()
                else:
                    echo_file_empty()
        except EXCEPTIONS as e:
            echo_file_error(e)
            echo_info_del_init()
    else:
        echo_file_not_found()
        echo_info_init()


@app.command()
def init(force: bool = typer.Option(False, "--force", "-f")) -> None:
    """Creates a cmd.yaml (if file exists, deletes
     (if --force (-f) is used) or leaves it)
    """
    if os.path.exists('cmd.yaml'):
        if force:
            os.remove("cmd.yaml")
            first_command = {"hi": "echo Hi from pcmd!"}
            save_cmd_yaml(first_command, 'w', False)
            echo_file_created()
        else:
            echo_file_exist()
    else:
        first_command = {"hi": "echo Hi from pcmd!"}
        save_cmd_yaml(first_command, 'w', False)
        echo_file_created()


@app.command()
def fish() -> None:
    """PCMD"""
    echo_fish(EGG)
    echo_fish(f"Version\t:\t{__version__}")
    echo_fish(f"Source\t:\t{URLS['github']}")
    echo_fish(f"Docs\t:\t{URLS['docs']}")
    echo_fish(f"Pypi\t:\t{URLS['pypi']}")
    echo_fish(f"Author\t:\t{URLS['author']}")


@app.command()
def add(
    key: str = typer.Option(..., '--key', '-k',
                            prompt="Enter custom name"),
    val: str = typer.Option(..., '--value', '-v',
                            prompt="Enter command")
) -> None:
    """
    Adds commands into the cmd.yaml using --key(-k) and --value(-v)
    """
    if os.path.exists('cmd.yaml'):
        tcommands = get_commands()
        if key in [*tcommands]:  # type: ignore
            typer.confirm('Custom name already exists.'
                          'Do you want to overwrite?',
                          abort=True)
            tcommands[key] = val  # type: ignore
            save_cmd_yaml(tcommands, 'w', True)
            echo_cmd_changed(key)
        else:
            add_load_and_save_echo(key, val)
    else:
        add_load_and_save_echo(key, val)
