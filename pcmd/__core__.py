"""
    __core__
    ~~~~~~~
    Core backend functions of pcmd.

    FUNCTIONS
    ~~~~~~~
    get_commands
    prettier
    save_cmd_yaml
    add_load_and_save_echo
    run_command
"""
import os
import yaml
import typer
import subprocess
from typing import Optional, Any
from .__echoes__ import echo_cmd_added


def get_commands() -> Optional[dict]:
    '''
    Parse yaml file and returns the commands in dict format.
    '''
    try:
        with open('cmd.yaml') as f:
            data = yaml.load(f, Loader=yaml.BaseLoader) or {}
            return data
    except FileNotFoundError:
        return None


def get_commands_list() -> list:
    '''
    Gets the custom names in a list
    '''
    commands = get_commands()
    if commands is None:
        return []
    else:
        return list(commands.keys())


def prettier(commands: dict) -> None:
    '''
    Option for list command. Prints the commands prettily.
    '''
    for key in commands:
        if type(commands[key]).__name__ == 'list':

            typer.secho(f"{key}\t: ",
                        fg=typer.colors.BLUE, bold=True)
            for command in commands[key]:
                typer.secho(f"\t- {command}",
                            fg=typer.colors.CYAN, bold=True)
        else:
            pretty_key = typer.style(f"{key}\t: ",
                                     fg=typer.colors.BLUE,
                                     bold=True)
            pretty_command = typer.style(commands[key],
                                         fg=typer.colors.CYAN,
                                         bold=True)
            typer.echo(pretty_key + pretty_command)


def save_cmd_yaml(data: Any, status: str, extra: bool) -> None:
    '''
    Saves data back to pcmd file depending on the write status.
    '''
    with open('cmd.yaml', status) as f:
        if extra is True:
            yaml.dump(data, f, sort_keys=False, indent=2)
        else:
            yaml.dump(data, f, sort_keys=False, indent=2)


def add_load_and_save_echo(key: str, val: str) -> None:
    '''
    Gets custom name and command and parses it to yaml object,
    , saves it and echoes info.
    '''
    data = yaml.load(f"\n{key}: {val}", Loader=yaml.BaseLoader)
    save_cmd_yaml(data, 'a', True)
    echo_cmd_added()


def run_command(cmd: str) -> None:
    '''
    Runs the commands using subprocess and chdir.
    '''
    if cmd.split(' ')[0] == 'cd':
        os.chdir(cmd.split(' ')[1].replace('\\', '\\\\'))
    else:
        subprocess.run(cmd.split(" "), shell=True)
