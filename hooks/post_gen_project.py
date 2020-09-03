import os


def delete_unnessary_packaging_file():
    to_remove_file = '{% if cookiecutter.packaging_tool == "conda" %} Pipfile {% else %} environment.yml {% endif %}'
    BASE_PATH = os.getcwd()
    full_path = os.path.join(BASE_PATH, to_remove_file.strip())
    os.remove(full_path)


if __name__ == '__main__':
    delete_unnessary_packaging_file()
