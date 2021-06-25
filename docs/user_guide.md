# User Guide
## Intro
We will go through the system requirements, commands, the `cmd.yaml` file, autocompletion, and other details.

## System requirements
 - [x] Works equally well on Windows, Linux and OSX.
 - [x] **pcmd** requires Python **3.6** and above.
??? Warning "Support for Python 2"
    Python 2 is **NOT** supported by pcmd
## Commands
### `init`
The `init` command creates the `cmd.yaml` file in the current working directory.  
???+ Note
    If the `cmd.yaml` already exists, it will leave the file as it is.
    To delete the file and create it again, use the  
    `--force (-f)` flag.  
    This can be useful when the file gets corrupted due to unfortunate circumstances.  
```bash
$ pcmd init

'cmd.yaml' created.
```
and the `cmd.yaml` will have,
```yaml
hi: echo Hi from pcmd!
```
---

### `add`
The `add` command lets you add single commands with custom name (an append operation).  

- `--key(-k)` - Adds custom name
- `--value(-v)` - Adds the command

Commands can also be interactively added by using just ```pcmd add```
```sh-ssession
$ pcmd add
Enter custom name: docker
Enter command: docker run
Command added in cmd.yaml
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
    If your file has encoding errors which cannot be resolved, you can start afresh using `init -f` command.
---
### `run`
This is the key command of **pcmd**.  
It runs your commands when given the specific custom name.
``` bash
$ pcmd run hi

Hi from pcmd! # this works since cmd.yaml had a custom name 'hi'
```
???+ Warning
    Commands which involve **changes** or **reload** of terminal will NOT work.  
    Some examples are,  
    - activating enviroments using `/env/Scripts/activate`  
    - Starting `python`, `node`, `mongo` or any other shell. The shell will open, but the commands after it will not work.  

    For more understanding, see some of the <a href="/examples" class="link">examples</a> provided.

???+ Tip "Technical details"
    Any commands which involve in the initiation of the child process will work in **pcmd**. The caveat is that the commands which are supposed to work in the child process will only work in the parent process, resulting in no command execution in the child process.

    For this reason, **pcmd** has a seperate functionality for the most-used `cd` command, which works perfectly fine.

---
### `list`
Lists the complete `cmd.yaml`.  
Useful to refer to commands rather than opening the `cmd.yaml`.  
```sh-session
$ pcmd list
        =======PCMD=======
Path    : path\to\project\cmd.yaml

c-and-p:
- git commit -m "small demo"
- git push
hi: echo Hi from pcmd!

```

 - `--pretty (-p)` : pretty prints the complete list (Useful for easier reading of large `cmd.yaml` files).

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
---
### `fish`  :material-egg-easter:
:fish: - ACSII Art of pcmd  
along with other useful links.

---
## `cmd.yaml` file
This is the file that should contain all your commands paired up with your custom name.  
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

???+ Tip "Useful tips in cmd.yaml"
    - You can always check the syntax of the `cmd.yaml` using `inspect` command.  
    - You can see the complete list of the file using `pcmd list -p` command.  
    - Avoid using same custom names for two different commands.

---
## Autocompletion from Typer
**pcmd** is built using *Typer*, which provides some stunning in-built autocompletion features.
For more details, check out their <a href="https://typer.tiangolo.com/tutorial/options/autocompletion/" class="link" target="_blank">docs</a>
???+ Note
    To Install autocompletion for the current shell.
    ```bash
    $ pcmd --install-completion
    ```

    To show completion for the current shell, to copy it or customize the installation.
    ```bash
    $ pcmd --show-completion
    ```

## Using `python -m`
pcmd can also be executed as a script. i.e.,
you can use `python -m` to execute the CLI.  
=== "python"

    ``` bash
    $ python -m pcmd init -f

    'cmd.yaml' created.
    ```

=== "python via poetry"

    ``` bash
    $ poetry run python -m pcmd init -f

    'cmd.yaml' created.
    ```

## Docs within CLI.
To check out **pcmd** docs within the CLI,
```bash
$ pcmd [COMMAND] --help
# Example: pcmd run --help
```

For full docs,

```bash
$ pcmd 
```
