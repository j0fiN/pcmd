"""
    trial_add
    ~~~~~~~
    Tryout of a new feature of add command

    FUNCTIONS
    ~~~~~~~
    run
    main
"""
from typing import Tuple


def run(command: str, args: Tuple[str]) -> None:
    '''
    Adds the arguments wherever $ symbol is found
    '''
    # print(command)
    for arg in args:
        command = command.replace('$', arg, 1)
    if command.count('$') > 0:
        print('All the $ are not filled | ERROR')
    else:
        print(command, '| RUNNING')


def main():
    cmd = "cd run $ swallow $"
    args = ('fall',)
    run(cmd, args)

    args = ('fall', 'winter')
    run(cmd, args)


if __name__ == "__main__":
    main()
