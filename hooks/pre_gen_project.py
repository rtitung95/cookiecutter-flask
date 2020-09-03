import re
import sys
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


def check_script_name():
    module_name = 'flask_{{cookiecutter.script_name.lower()}}'
    if not re.match(MODULE_REGEX, module_name):
        print("ERROR: {} is not a valid Python module name!".format(module_name))
        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == '__main__':
    check_script_name()
