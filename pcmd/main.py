import yaml
import typer
import os
from pathlib import Path

app = typer.Typer()


@app.callback()
def callback():
    """
    A super simple terminal command shortener

    Simple example:
    1. Create file cmd.yaml and type\n
        hi: echo "Hi from pcmd!"

    2. From the same dir, in your terminal, type\n
        pcmd run hi
    """

def get_commands():
    try:
        with open(os. getcwd()+'\\cmd.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except FileNotFoundError:
        return None

@app.command()
def run(command: str):
    commands = get_commands()
    if commands is None:
        typer.secho("FileNotFound: Please make sure that your file name is 'cmd.yaml'", fg=typer.colors.RED, bold=True)
    else:
        try:
            cmds = commands[command]
            if type(cmds).__name__ == 'list':
                for cmd in cmds:
                    os.system(cmd)
            else:
                os.system(commands[command])
        except KeyError:
            typer.secho("CommandNotFound: Please make sure that you have assigned a command to this name in 'cmd.yaml'", fg=typer.colors.RED, bold=True)
