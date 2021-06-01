# THESE FUNCTIONS ARE FOR CLI's BACKEND
import yaml
import typer
from typing import Dict, List, Optional, Union, Any


def get_commands() -> Optional[Dict[str, Union[List[str], str]]]:
    try:
        with open('cmd.yaml') as f:
            data = yaml.load(f, Loader=yaml.BaseLoader) or {}
            return data
    except FileNotFoundError:
        return None


def prettier(commands: dict) -> None:
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
    with open('cmd.yaml', status) as f:
        if extra is True:
            yaml.dump(data, f, sort_keys=False, indent=2)
        else:
            yaml.dump(data, f, sort_keys=False, indent=2)
