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
print-hi: echo "Hi from pcmd!"
dir-check: dir
```
### That's it! :tada:
Now (from the same directory where `cmd.yaml` exists)  type
```bash
$ pcmd run print-hi
```
It outputs
```bash
$ Hi from pcmd!
```

### For more docs :page_facing_up:
```bash
$ pcmd
```

## Usage 🧰
> The main usage where you can ***pcmd*** is during developement, where multiple long terminal commands may be used repeadetly in different order.It can be frustating to type long commands when you start up the terminal for the day or when a terminal shuts down due to unknown reasons!  

---
<p align=center>Do throw a :star: if you like the package!</p>
