import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='.')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ajax')
def ajax():
    a = request.args.get('a', 1, type=int)
    b = request.args.get('b', 100, type=int)
    rand = random.randint(a, b)
    return jsonify(result=rand)


if __name__ == '__main__':
    app.run(debug=True)
