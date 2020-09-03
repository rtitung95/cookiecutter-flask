# Cookiecutter Flask Sample boilerplate

## Quick Installation
1. Install cookiecutter

  ```bash
  pip install cookiecutter
  ```
2. Generate the boilerplate

  ```bash
  cookiecutter https://github.com/rtitung95/cookiecutter-flask.git
  ```

## Cookiecutter Project structure

    ├── cookiecutter-flask
        ├── cookiecutter.json
        ├── README.md
        ├── {{cookiecutter.app_name.lower() | replace(' ', '_') | replace('-', '_')}}
        │   ├── environment.yml
        │   ├── flask_{{cookiecutter.script_name.lower()}}.py
        │   ├── Pipfile
        │   └── README.md
        │
        └── hooks
            ├── pre_gen_project.py
            │
            └── post_gen_project.py
