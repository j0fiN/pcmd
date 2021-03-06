"""
    __const__
    ~~~~~~~
    Constants of pcmd.

    CONSTANTS
    ~~~~~~~
    EGG
    URLS
    EXCEPTIONS
"""
import yaml  # type: ignore


EGG = """
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


URLS = {
    'github': 'https://github.com/j0fiN/pcmd',
    'pypi': 'https://pypi.org/project/pcmd/',
    'docs': 'https://j0fin.github.io/pcmd/',
    'author': 'https://jofin.herokuapp.com/'
}


EXCEPTIONS = (yaml.reader.ReaderError,
              yaml.scanner.ScannerError,
              yaml.YAMLError)


PATTERN = "<[0-9]>"
