# pcmd
<img alt="PyPI" src="https://img.shields.io/pypi/v/pcmd?logo=pypi&logoColor=white&style=flat-square"> <img alt="PyPI - License" src="https://img.shields.io/pypi/l/pcmd?style=flat-square"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pcmd?logo=python&logoColor=white&style=flat-square">  
 _A super simple terminal command shortener Cli._ :tada:


## Usage 🧰
During developement, it can be frustating to type long commands when you start up the terminal for the day or when a terminal shuts down due to unknown reasons!
There might be times when you had to type a set of long terminal commands repeatedly.  

> For all these problems...  
  
***pcmd*** comes in handy :+1:  
- It helps to execute commands with user-define name :fish:
- It helps to execute multiple commands with just a single command of user-defined name :octopus:

## Getting started :rocket:
### Install the package :package:
Using _pip_
```sh-session
$ pip insall pcmd

---> 100%
```
or from _poetry_,
```sh-session
$ poetry add pcmd

---> 100%
```
or download the  files from the [releases](https://github.com/j0fiN/pcmd/releases) :bookmark:.
### Building a `cmd.yaml` file :hammer:
Create a file `cmd.yaml` (make sure you create it with a proper text editor).  
The key will be your custom name and value will be the terminal command.  
```<custom name>: <terminal command>```  
Here we see a simple example,
```yaml
print-hi: echo "An example of a long command depicting usage of pcmd!"
dir-check: dir
```
### That's it! :fish:
Now (from the same directory where `cmd.yaml` exists)  type,
```sh-session
pcmd run print-hi
```
It outputs
```text
$ An example of a long command depicting usage of pcmd!
```

### Running multiple command lines :octopus:
You can also run multiple commands from a single custom command using **pcmd**.  
In `cmd.yaml`,  
```yaml
git-list:
  - git add .
  - git commit -m 'Added feature to run multiple commands'
  - git push
```
> :warning: WARNING: Commands which involve *changes or reload of terminal* (Eg: `cd` and _activating enviroments_ using `/env/Scripts/activate`) **may NOT WORK** due to break in command flow.  
> It will be fixed in the next version.  

Now type,  
```sh-session
pcmd run git-list
```

### For more docs :page_facing_up:
```sh-session
pcmd
```

---
<p align=center>Do throw a :star: if you like the package!</p>
