# Development - Contributing

Before diving into the code, here are some guidelines for contribution.

## Installation
For any contribution (doc or code), the latest version of **pcmd** must be installed globally first,
```bash
$ pip install pcmd
```

**pcmd** uses,

 - [x] poetry           - Build, package and publish the project.
 - [x] pytest           - Build tests.
 - [x] flake8           - Code style guide.
 - [x] mypy             - Type checking.
 - [x] coverage         - Test coverage.
 - [x] mkdocs-material  - Documentation.

All these can be downloaded as extras in **pcmd** in your *virtual environment*.

=== "pip"
    ```bash
    $ pip install poetry
    ---> 100%

    $ pip install pcmd[dev]
    ---> 100%
    ```

=== "poetry"

    ``` bash
    $ poetry add pcmd[dev]



    ---> 100%     
    ```

## Developement
Add `app()` at the end of the `\pcmd\main.py` file to test your changes in terminal.  

The `cmd.yaml` in the root directory has single-letter commands for each command in **pcmd**
```bash
$ pcmd run r # run command

$ pcmd run i # inspect command

$ pcmd list -p # check out the other commands too
```

## Pre-Commit check
The `cmd.yaml` in the root directory has a command chain with the name `check`
```bash
$ pcmd run check
```

This will run

- pytest tests
- flake8 checks
- mypy inspection (if specified)
- code coverage.

Making things much easier!

## Documentation
The `cmd.yaml` in the root directory has command named `doc` to test the documentation
in the local server.
```bash
pcmd run doc
```
