"""
    tryout_run_args
    ~~~~~~~
    Tryout of a new feature of run command arguments

    FUNCTIONS
    ~~~~~~~
    run
    main
"""
import re
import os
import subprocess
# from __echoes__ import *
# from __core__ import echo_cmd_not_found



PATTERN = "<[0-9]>"
def contains_arguments(command: str) -> bool:
    return False if re.findall(PATTERN, command) == [] else True
    

def run_command(cmd: str, args: list = []) -> None:
    '''
    Runs the commands using subprocess and chdir.
    '''
    if cmd.split(' ')[0] == 'cd':
        os.chdir(cmd.split(' ')[1].replace('\\', '\\\\'))
    else:
        subprocess.run(cmd.split(" "), shell=True)



# @app.command()
def run(command: str) -> None:
    """
    Run terminal command / runs multiple command chains.\n
    Check docs for warnings ('$ pcmd fish' for link).
    """
    commands = {'hi Hello': 'echo <1>'}
    if commands is None:
        print("File not Found")
    else:
        try:
            cmds = commands[command]
            if type(cmds).__name__ == 'list':
                for cmd in cmds:
                    run_command(cmd)
            else:
                run_command(cmds)
        except KeyError:
            # echo_cmd_not_found(command)
            ...