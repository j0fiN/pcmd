# pcmd

:sparkles: A super simple terminal command shortner.

# Getting started
## Install the package
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
## Building a cmd.yaml file
Create a file `cmd.yaml` or `cmd.yaml`.  
Here we see a simple example
```yaml
print-hi: echo "Hi from pcmd!"
dir-check: dir
```
## That's it!
Now (from the same directory where `cmd.yaml` exists)  type
```bash
$ pcmd run print-hi
```
It outputs
```bash
$ Hi from pcmd!
```


