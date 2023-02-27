import requests
from requests.models import Response
from flask import (
    Flask,
    Response
    )

from flask.app import Flask as FlaskApp


app: FlaskApp = Flask(__name__)

@app.route("/")
def main_page() -> str:
    return 'This is Flask Calculator!!! Add to the protocol /numberone/+ or - or * or / or %/numbertwo'

@app.route('/<int:num1>/<token>/<int:num2>')
def article(num1: int, num2: int, token: str):
    try:
        if token == "+":
            return f'{num1} + {num2} = {num1 + num2}'
        elif token == "-":
            return f'{num1} - {num2} = {num1 - num2}'
        elif token == "*":
            return f'{num1} * {num2} = {num1 * num2}'
        elif token == "--":
            return f'{num1} / {num2} = {num1 / num2}'
        elif token == "%":
            return f'{num1} % {num2} = {num1 % num2}'
        else:
            return 'wrong'
    except:
        return "No zero"

if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    ) 