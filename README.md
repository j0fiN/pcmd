# pcmd

:sparkles: A super simple terminal command shortner.

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
### Building a cmd.yaml file :bulb:
Create a file `cmd.yaml`.  
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
## Usage :memo:
> The main usage where you can ***pcmd*** is during developement, where multiple long terminal commands may be used repeadetly in different order.It can be frustating to type long commands when you start up the terminal for the day or when a terminal shuts due to unknown reasons!

