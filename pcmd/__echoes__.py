"""
    __echoes__
    ~~~~~~~
    Functions of typer.echo() and typer.secho() function

    FUNCTIONS
    ~~~~~~~
    echo_file_not_found
    echo_file_created
    echo_file_exist
    echo_file_empty
    echo_file_found
    echo_file_error
    echo_file_valid
    echo_cmd_changed
    echo_cmd_added
    generate_path
    echo_list_header
    echo_inspect_header
    echo_info_del_init
    echo_info_init
    echo_fish
    echo_args_not_found_error
    echo_argument_limit_error
"""
import typer
import os


def echo_file_not_found():
    typer.secho("FileNotFound: Please make sure "
                "that your file name is cmd.yaml",
                fg=typer.colors.RED,
                bold=True,
                err=True)


def echo_file_created():
    typer.secho("cmd.yaml created.",
                fg=typer.colors.CYAN,
                bold=True)


def echo_file_exist():
    typer.secho("'cmd.yaml' already exists.",
                fg=typer.colors.GREEN,
                bold=True)


def echo_file_empty():
    typer.secho("\t'cmd.yaml' is empty. Please "
                "enter any command into the file.",
                fg=typer.colors.YELLOW,
                bold=True)


def echo_file_found():
    typer.secho("\t'cmd.yaml' file found!\n",
                fg=typer.colors.GREEN,
                bold=True)


def echo_file_error(e):
    typer.secho(f"\tERROR in file : \n{e}",
                fg=typer.colors.RED,
                bold=True)


def echo_file_valid():
    typer.secho("\t'cmd.yaml' is valid!",
                fg=typer.colors.GREEN,
                bold=True)


def echo_cmd_changed(key):
    typer.secho("Command changed for name "
                f"'{key}' in cmd.yaml",
                fg=typer.colors.CYAN,
                bold=True)


def echo_cmd_added():
    typer.secho("Command added in cmd.yaml",
                fg=typer.colors.CYAN,
                bold=True)


# Command specific Echoes
def generate_path():
    os.path.join(os.getcwd(), 'cmd.yaml').replace('\\\\', '\\')


def echo_list_header():
    typer.secho(f"\t=======PCMD=======\n"
                f"Path\t:{generate_path()}\n",
                fg=typer.colors.BLUE,
                bold=True)


def echo_inspect_header():
    typer.secho("PCMD Inspection : ",
                fg=typer.colors.BLUE,
                bold=True)


# Info echoes
def echo_info_del_init():
    typer.secho("INFO : Delete the file and type "
                "'pcmd init' to create cmd.yaml file",
                fg=typer.colors.CYAN,
                bold=True)


def echo_info_init():
    typer.secho("INFO : Type 'pcmd init' to "
                "create cmd.yaml file",
                fg=typer.colors.CYAN,
                bold=True)


def echo_fish(string: str):
    typer.secho(string,
                fg=typer.colors.CYAN,
                bold=True)


# Arguments feature echoes.
def echo_args_not_found_error(cmd: str):
    typer.secho(f"\tERROR : Arguments not provided for the command \n{cmd}",
                fg=typer.colors.RED,
                bold=True)


def echo_argument_limit_error():
    typer.secho("\tERROR : only 10 arguments allowed.",
                fg=typer.colors.RED,
                bold=True)
