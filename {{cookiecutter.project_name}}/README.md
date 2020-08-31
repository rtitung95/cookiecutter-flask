## {{cookiecutter.app_name}}

## Quick Installation
1. Install cookiecutter

  ```bash
  pip install cookiecutter
  ```
2. Generate the boilerplate

  ```bash
  cookiecutter https://github.com/rtitung95/cookiecutter-flask.git
  ```

## Instructions
1. Create (and activate) a new environment from  `Pipfile` file. Navigate to this file location or folder `./{{cookiecutter.project_name}}` and find `Pipfile` file and follow following instructions.
  ```bash
  pipenv install
  pipenv shell
  ```
2. Run the flask application
  ```bash
  python {{cookiecutter.script_file_name}}.py
  ```
