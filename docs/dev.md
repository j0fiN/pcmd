# Development - Contributing

Before diving into the code, here are some guidelines for contribution.

## Installation
For any contribution (doc or code), **pcmd** must be installed globally.  
This installation will be for working with `cmd.yaml` which has some useful commands for developement.

```bash
$ pip install pcmd
```
Now,  
**pcmd** uses,

 - [x] poetry           - *Build, package and publish the project*
 - [x] pytest           - *Build tests*
 - [x] flake8           - *Code style guide*
 - [x] mypy             - *Type checking*
 - [x] coverage         - *Test coverage*
 - [x] pytest-cov       - *For coverage in pytest*
 - [x] mkdocs-material  - *Documentation*

All these can be downloaded as extras in **pcmd** in your *virtual environment* (except for poetry, which is the developer's choice).

=== "pip"
    ```bash
    $ pip install poetry
    ---> 100% # optional

    $ pip install pcmd[dev]
    ---> 100%
    ```

=== "poetry"

    ``` bash
    $ poetry add pcmd[dev]



    ---> 100%     
    ```

## Developement
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
- code coverage (with the number of lines not covered).

Making things much easier!

## Documentation
The `cmd.yaml` in the root directory has command named `doc` to test the documentation
in the local server.
```bash
pcmd run doc
```

## Conclusion
Do follow the [gitmoji](https://gitmoji.dev/) style of commit messages.  

Do fork the repo and come up with crazy PRs!

---

<p align="center">Do 🌟 the repo if you like it!</p>