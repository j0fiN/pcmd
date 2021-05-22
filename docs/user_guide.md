# User Guide
## Intro
We will go through the sys requirements, commands, the `cmd.yaml` file and autocompletion.

## System requirements
 - [x] Works equally well on Windows, Linux and OSX.
 - [x] **pcmd** requires Python **3.6** and above.
??? Warning "Support for Python 2"
    Python 2 is **NOT** supported by pcmd
## Commands
### `init`
The `int` command creates the `cmd.yaml` file in the current working directory.  
???+ Note
    If the `cmd.yaml` already exists, it will **delete** the file and create it again.
    This is useful when the `cmd.yaml` gets corrupted due to unfortunate circumstances.  
```bash
$ pcmd init

'cmd.yaml' created.
```
and the `cmd.yaml`,
```yaml
hi: echo Hi from pcmd!
```
### `inspect`
Inspects if `cmd.yaml` exists and if there are any *syntax* errors or *encoding* errors.
```sh-ssession
$ pcmd inspect

PCMD Inspection : 
        'cmd.yaml' file found!

        'cmd.yaml' is valid!

```

???+ Tip
    If your file is has encoding errors which cannot be resolved, you can start afresh using `init` command.
### `run`
This is key command of **pcmd**.  
It runs your commands when given the specific custom name.
``` bash
$ pcmd run hi

Hi from pcmd!
```
???+ Warning
    Commands which involve **changes** or **reload** of terminal will NOT WORK.  
    Some examples are,  
    - activating enviroments using `/env/Scripts/activate`  
    - `cd` command

### `list`
Lists the complete `cmd.yaml`.  
Useful to refer commands rather than opening the `cmd.yaml`.  
```sh-session
$ pcmd list
        =======PCMD=======
Path    : path\to\project\cmd.yaml

c-and-p:
- git commit -m "small demo"
- git push
hi: echo Hi from pcmd!

```

 - `--pretty (-p)` : pretty prints the complete list (Useful for easier reading of large `cmd.yaml` files)

    ???+ Example
        ```sh-session
        $ pcmd list -p
                =======PCMD=======
        Path    : path\to\project\cmd.yaml

        hi      : echo Hi from pcmd!
        c-and-p :
                - git commit -m "small demo"
                - git push

        ```

### `fish`  :material-egg-easter:
:fish: - ACSII Art of pcmd

## `cmd.yaml` file
This is file which should contain all your commands paired up with your custom name.  
!!! Note 
    If file is created manually, it must be named `cmd.yaml` and NOT `cmd.yml`

For single commands, type in the format of `<name>: <command>`.
```yaml
hi : echo hi from pcmd!
check : poetry run pytest 
```

For multiple commands, type the `<name>`, along with the list of command using the hyphen(`-`) symbol. 
```yaml
c-init:
  - git commit -m 'init commit'
  - git push
```
???+ Tip
    You can always check the syntax of the `cmd.yaml` using `inspect` command.  
    You can see the complete list of the file using `pcmd list -p` command.


## Autocompletion from Typer
**pcmd** is built using *Typer*, which provides some stunning in-built auto completion features.
For more details, check out their <a href="https://typer.tiangolo.com/tutorial/options/autocompletion/" class="link" target="_blank">docs</a>
???+ Warning
    Auto completion feature may not work in some terminals.
