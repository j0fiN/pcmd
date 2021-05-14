# pcmd
<img alt="PyPI" src="https://img.shields.io/pypi/v/pcmd?logo=pypi&logoColor=white&style=flat-square"> <img alt="PyPI - License" src="https://img.shields.io/pypi/l/pcmd?style=flat-square"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pcmd?logo=python&logoColor=white&style=flat-square">  
:sparkles: _A super simple terminal command shortener Cli._ :sparkles:

## Getting started :rocket:
### Install the package :package:
Using _pip_
```bash
$ pip insall pcmd

---> 100%
```
or from _poetry_,
```bash
$ poetry add pcmd

---> 100%
```
### Building a cmd.yaml file :hammer:
Create a file `cmd.yaml`.  
The key will be your custom name and value will be the terminal command.
```<custom name>: <terminal command>```  
Here we see a simple example
```yaml
print-hi: echo "An example of a long command depicting usage of pcmd!"
dir-check: dir
```
### That's it! :tada:
Now (from the same directory where `cmd.yaml` exists)  type
```bash
$ pcmd run print-hi
```
It outputs
```console
$ An example of a long command depicting usage of pcmd!
```

### Running multiple command lines
You can also run multiple commands from a single custom command using **pcmd**
```yaml
# cmd.yaml
get-started:
  - git clone https://github.com/j0fiN/Iris-Says.git
  - cd Iris-Says
  - pip install -r requirements.txt
  - python run.py
```
> Warning: Commands which involve _changes or reload of terminal_(Eg: _activating enviroments_ using `./env/Scripts/activate`) **may not work** due to break in command flow.
```bash
$ pcmd run get-started
```

### For more docs :page_facing_up:
```bash
$ pcmd
```

## Usage 🧰
> The main usage where you can ***pcmd*** is during developement, where multiple long terminal commands may be used repeatedtly in different order. It can be frustating to type long commands when you start up the terminal for the day or when a terminal shuts down due to unknown reasons!  

---
<p align=center>Do throw a :star: if you like the package!</p>
