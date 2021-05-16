import yaml
import typer
import os
from pathlib import Path
import subprocess
app = typer.Typer()

egg = """
|\   \\\\__     o
| \_/    o \    o 
> _   (( <_  oo  
| / \__+___/      
|/     |/
                             _
 _ __    ___  _ __ ___    __| |
| '_ \  / __|| '_ ` _ \  / _` |
| |_) || (__ | | | | | || (_| |
| .__/  \___||_| |_| |_| \__,_|
|_|

"""

@app.callback()
def callback():
    """
    A super simple terminal command shortener\n

    For docs : https://github.com/j0fiN/pcmd
    """

def get_commands():
    try:
        with open('cmd.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except FileNotFoundError:
        return None

@app.command()
def run(command: str):
    """
    run command - run terminal command/ runs multiple command chains
    """
    commands = get_commands()
    if commands is None:
        typer.secho("FileNotFound: Please make sure that your file name is 'cmd.yaml'", fg=typer.colors.RED, bold=True)
    else:
        try:
            cmds = commands[command]
            if type(cmds).__name__ == 'list':
                for cmd in cmds:
                    subprocess.run(cmd.split(" "), shell=True)
            else:
                os.system(commands[command])
        except KeyError:
            typer.secho("CommandNotFound: Please make sure that you have assigned a command to this name in 'cmd.yaml'", fg=typer.colors.RED, bold=True)

@app.command()
def list():
    """
    list command - outputs the cmd.yaml 
    """
    commands = get_commands()
    if commands is None:
        typer.secho("FileNotFound: Please make sure that your file name is 'cmd.yaml'", fg=typer.colors.RED, bold=True)
    else:
        typer.secho(f"PCMD\nFile Path : {os. getcwd()}\\cmd.yaml".replace('\\\\', '\\'), fg=typer.colors.MAGENTA, bold=True)
        typer.echo(yaml.dump(commands))
        

@app.command()
def fish():
    typer.secho(egg, fg=typer.colors.MAGENTA, bold=True)