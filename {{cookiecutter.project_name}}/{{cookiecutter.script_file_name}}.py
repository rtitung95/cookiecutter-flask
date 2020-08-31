from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    ret = "Hello, {{cookiecutter.name}}!"
    return ret


if __name__ == '__main__':
    app.run()
