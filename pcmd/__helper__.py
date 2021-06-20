"""
    __helper__
    ~~~~~~~
    Helper functions for unittesting pcmd.

    FUNCTIONS
    ~~~~~~~
    f_remove
    f_add
    f_syntax_err
    f_scan_err
    f_empty
"""
import os
import yaml


def f_remove():
    os.remove('cmd.yaml')


def f_add(commands):
    with open('cmd.yaml', 'w') as f:
        yaml.dump(commands, f, sort_keys=False, indent=2)


def f_syntax_err():
    with open('cmd.yaml', 'w') as f:
        f.write("error: [][")


def f_scan_err():
    with open('cmd.yaml', 'w') as f:
        yaml.dump({'err': 'err'}, f)
        yaml.dump("\nerr: arr'", f)


def f_empty():
    with open('cmd.yaml', 'w') as f:
        f.write("")
