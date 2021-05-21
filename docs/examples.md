# Examples
blah - Copy the one you need.
```yaml
# A simple project initiation
git:
 - git clone <link>
 - cd <project name> # Not yet built
 - nodemon start

# Multiple commands demonstration
list:
  - echo "git init"
  - echo "git add ."
  - echo "git commit -m 'Added feature to run multiple commands'
  - echo "git push"



# Checks before commits
check:
  - poetry run pytest
  - echo ----------------------
  - echo Flake test
  - flake8
  - echo ----------------------
  - echo mypy test
  - mypy .
```
A footnote saying that the examples here work if only configured already. Eg: poetry command won't work if you don't have poetry installed!