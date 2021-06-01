import yaml
import typer
import os  # type: ignore
import subprocess
from typing import Dict, List, Optional, Union
from collections import OrderedDict
app = typer.Typer()

egg = """
|\\   \\\\\\\\__     o
| \\_/    o \\    o
 > _   (( <_  oo
| / \\__+___/
|/     |/
                             _
 _ __    ___  _ __ ___    __| |
| '_ \\  / __|| '_ ` _ \\  / _` |
| |_) || (__ | | | | | || (_| |
| .__/  \\___||_| |_| |_| \\__,_|
|_|

"""


# THESE FUNCTIONS ARE FOR TESTING PURPOSES
def f_remove():
    os.remove('cmd.yaml')


def f_add(commands):
    with open('cmd.yaml', 'w') as f:
        yaml.dump(commands, f)


def f_syntax_err():
    with open('cmd.yaml', 'w') as f:
        f.write("error: [][")


def f_reader_err():
    with open('cmd.yaml', 'w', encoding='ascii') as f:
        f.write(" ")


def f_empty():
    with open('cmd.yaml', 'w') as f:
        f.write("")


# THESE FUNCTIONS ARE FOR CLI's BACKEND
def get_commands() -> Optional[Dict[str, Union[List[str], str]]]:
    try:
        with open('cmd.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader) or {}
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


# THESE FUNCTIONS ARE FOR CLI's COMMANDS
@app.callback()
def callback() -> None:
    """
    PCMD\n
    A super simple terminal command shortener\n
    Version : v2.1.0\n
    Source : https://github.com/j0fiN/pcmd
    """


@app.command()
def run(command: str) -> None:
    """
    Run terminal command / runs multiple command chains.\n
    Check docs for warnings (pcmd fish for link).
    """
    commands = get_commands()
    if commands is None:
        typer.secho("FileNotFound: Please make sure that your "
                    "file name is 'cmd.yaml'",
                    fg=typer.colors.RED, bold=True, err=True)
    else:
        try:
            cmds = commands[command]
            if type(cmds).__name__ == 'list':
                for cmd in cmds:
                    if cmd.split(" ")[0] == "cd":  # type: ignore
                        os.chdir(cmd.split(" ")[1].replace('\\', '\\\\'))
                    else:
                        subprocess.run(cmd.split(" "), shell=True)
            else:
                if cmds.split(" ")[0] == "cd":  # type: ignore
                    os.chdir(
                        cmds.split(" ")[1].replace('\\',  # type: ignore
                                                   '\\\\'))
                else:
                    subprocess.run(cmds.split(" "), shell=True)  # type: ignore
        except KeyError:
            typer.secho("CommandNotFound: Please make sure that you have"
                        " assigned a command to this name in 'cmd.yaml'",
                        fg=typer.colors.RED, bold=True, err=True)


@app.command()
def list(
    pretty: bool = typer.Option(False, "--pretty", "-p")
) -> None:
    """
    Outputs the complete cmd.yaml (use -p for pretty).
    """
    commands = get_commands()
    if commands is None:
        typer.secho("FileNotFound: Please make sure that "
                    "your file name is 'cmd.yaml'",
                    fg=typer.colors.RED, bold=True)
    else:
        typer.secho(f"\t=======PCMD=======\nPath\t: {os. getcwd()}\\"
                    "cmd.yaml\n".replace('\\\\', '\\'),
                    fg=typer.colors.BLUE, bold=True)
        if commands == {}:
            typer.secho("\t'cmd.yaml' is empty. Please "
                        "enter any command into the file.",
                        fg=typer.colors.YELLOW,
                        bold=True)
        else:
            if pretty:
                prettier(commands)
            else:
                typer.echo(yaml.dump(commands, indent=4,
                                     explicit_start=True,
                                     explicit_end=True))


@app.command()
def inspect() -> None:
    """Checks if cmd.yaml exists and validates it."""
    typer.secho("PCMD Inspection : ", fg=typer.colors.BLUE,
                bold=True)
    if os.path.exists('cmd.yaml'):
        typer.secho("\t'cmd.yaml' file found!\n",
                    fg=typer.colors.GREEN,
                    bold=True)
        try:
            with open('cmd.yaml', 'r') as f:
                data = yaml.load(f, Loader=yaml.SafeLoader)
                if data is not None:
                    typer.secho("\t'cmd.yaml' is valid!",
                                fg=typer.colors.GREEN,
                                bold=True)
                else:
                    typer.secho("\t'cmd.yaml' is empty. Please "
                                "enter any command into the file.",
                                fg=typer.colors.YELLOW,
                                bold=True)

        except yaml.YAMLError as e:
            typer.secho(f"\tERROR in file : \n{e}",
                        fg=typer.colors.RED,
                        bold=True)
        except (UnicodeDecodeError, yaml.reader.ReaderError) as e:
            typer.secho(f"\tERROR in file : /n/t{e}",
                        fg=typer.colors.RED,
                        bold=True)
            typer.secho("INFO : Delete the file and type "
                        "'pcmd init' to create cmd.yaml file",
                        fg=typer.colors.CYAN,
                        bold=True)
    else:
        typer.secho("'cmd.yaml' file NOT found",
                    fg=typer.colors.RED,
                    bold=True)
        typer.secho("INFO : Type 'pcmd init' to create cmd.yaml file",
                    fg=typer.colors.CYAN,
                    bold=True)


@app.command()
def init(force: bool = typer.Option(False, "--force", "-f")) -> None:
    """Creates a cmd.yaml (if file exists, deletes
     (if --force (-f) is used) or leaves it)."""
    if os.path.exists('cmd.yaml'):
        if force:
            os.remove("cmd.yaml")
            first_command = {"hi": "echo Hi from pcmd!"}
            with open('cmd.yaml', 'w') as f:
                yaml.dump(first_command, f)
                typer.secho("'cmd.yaml' created.",
                            fg=typer.colors.CYAN, bold=True)
        else:
            typer.secho("'cmd.yaml' already exists.",
                        fg=typer.colors.GREEN, bold=True)
    else:
        first_command = {"hi": "echo Hi from pcmd!"}
        with open('cmd.yaml', 'w') as f:
            yaml.dump(first_command, f)
            typer.secho("'cmd.yaml' created.",
                        fg=typer.colors.CYAN, bold=True)


@app.command()
def fish() -> None:
    """PCMD"""
    typer.secho(egg, fg=typer.colors.CYAN, bold=True)
    typer.secho("Source\t:\thttps://github.com/j0fiN/pcmd",
                fg=typer.colors.CYAN,
                bold=True)
    typer.secho("Docs\t:\thttps://j0fin.github.io/pcmd/",
                fg=typer.colors.CYAN,
                bold=True)
    typer.secho("Pypi\t:\thttps://pypi.org/project/pcmd/",
                fg=typer.colors.CYAN,
                bold=True)
    typer.secho("Author\t:\thttps://jofin-f-archbald.herokuapp.com/",
                fg=typer.colors.CYAN,
                bold=True)

@app.command()
def add(
    key:str = typer.Option(..., '--key', '-k', 
                           prompt="Enter custom name"),
    val:str = typer.Option(..., '--value', '-v',
                           prompt="Enter command")
) -> None:
    """
    Adds commands into the cmd.yaml using --key(-k) and --value(-v)
    """
    commands = get_commands()
    if key in list(commands.keys()):
        conf = typer.confirm('Custom name already exists.'
                             'Do you want to overwrite?', 
                             abort=True)
        commands[key] = val

    with open('cmd.yaml', 'a') as f:
        yaml.dump({key: val}, f)
    
    typer.secho("Command added in cmd.yaml",
                fg=typer.colors.CYAN,
                bold=True)
