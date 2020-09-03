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

## Project structure

    ├── {{cookiecutter.app_name.lower() | replace(' ', '_') | replace('-', '_')}}
        ├── {% if cookiecutter.packaging_tool== "pipenv" %} Pipfile {% else %} environment.yml {% endif%}
        |
        ├── flask_{{cookiecutter.script_name.lower()}}.py
        │
        └── README.md


## Instructions
{% if cookiecutter.packaging_tool== "pipenv" %}
1. Create (and activate) a new environment from  `Pipfile` file. Navigate to this file location or folder `./{{cookiecutter.app_name.lower() | replace(' ', '_') | replace('-', '_')}}` and find `Pipfile` file and follow following instructions.
  ```bash
  pipenv install
  pipenv shell
  ```
{% else %}
1. Create (and activate) a new environment from  `environment.yml` file. Navigate to this file location or folder `./{{cookiecutter.app_name.lower() | replace(' ', '_') | replace('-', '_')}}` and find `environment.yml` file and follow following instructions.
  - __Linux__ or __Mac__:
  ```bash
  conda env create -f environment.yml
  source activate {{cookiecutter.app_name.lower().replace(' ', '_').replace('-', '_')}}
  ```
  - __Windows__:
  ```bash
  conda env create -f environment.yml
  activate {{cookiecutter.app_name.lower().replace(' ', '_').replace('-', '_')}}
  ```
{% endif %}
2. Run the flask application
  ```bash
  python flask_{{cookiecutter.script_name.lower()}}.py
  ```
