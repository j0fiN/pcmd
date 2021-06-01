#  Functions for testing purposes.
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
