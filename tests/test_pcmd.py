from pcmd import __version__
from pcmd.main import get_commands

def test_version():
    assert __version__ == '1.2.3'

def test_get_commands_1():
    assert type(get_commands()).__name__ == "dict"

def test_get_commands_2():
    assert get_commands()['test'] == "dir"

def test_get_commands_3():
    try:
        a = get_commands()['test-3']
    except:
        a = None
    assert a == None

def test_get_commands_4():
    assert type(get_commands()['lst']).__name__ == "list"
