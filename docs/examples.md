# Examples
Here are a few examples of how you can use **pcmd**.  

```yaml
# SINGLE COMMANDS
hi: echo hello from pcmd!

# Running files deep inside the project in poetry
run-poetry: poetry run python a\long\path\to\a\file.py
# Using python
run-py: python a\long\path\to\a\file.py



# MULTIPLE COMMANDS
list:
  - echo git init
  - echo git add .
  - echo git commit -m 'Added feature to run multiple commands'
  - echo git push

# Sample project initiations from github
node-github:
 - git clone <link>
 - cd <project name>
 - npm install
 - nodemon start

flask-github:
 - git clone <link>
 - cd <project name>
 - pip install -r requirements.txt
 - py app.py

# An Alternative for requirements.txt !
install:
  - pip install pcmd
  - pip install fastapi
  - pip install tensorflow

# Commands which has prompts
prompt:
  - pip install utile==1.0
  - pip uninstall utile # This is a command with a user confirmation
  - pip install utile==1.0

# pre-commit checks are useful for open-source projects, 
# which has various tests, checks and reports.
check:
  - poetry run pytest --cov
  - echo ----------------------
  - echo Flake test
  - flake8
  - echo ----------------------
  - echo mypy test
  - mypy .

# Check API endpoints
user-1: curl http://localhost:5000/user/1
# Checking multiple endpoints using a single custom command !
user-all:
  - curl http://localhost:5000/user/1
  - curl http://localhost:5000/user/1/profile
  - curl http://localhost:5000/user/1/blogs
  - curl http://localhost:5000/user/1/followers


# ==================================
# Commands which Do NOT work ❌
py:
  - py # Python Shell is opened (this applies any shell; node, mongo, etc)
  - print('Hello') # This does not work within the shell ❌
  - exit() # This does not work within the shell ❌

activate:
  - py -m venv env # env is created
  - /env/Scripts/activate # but CANNOT be activated in the terminal ❌
  - pip install -r requirements.txt # since previous does not work, 
# this will install the packages globally (which is a mess!)

```

!!! Note
    Examples here work only if configured already.  
    An example: `poetry` command won't work if you don't have poetry installed!