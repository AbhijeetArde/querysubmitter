import random
from flask import Flask, render_template, jsonify, request
import datetime

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


@app.route('/live')
def pre():
    import random
    data = random.randint(0, 50)
    data2 = random.randint(0, 500)

    now = datetime.datetime.now().strftime("%H:%M:%S")
    return jsonify(result=data, result2=now, result3=data2, result4=now)


if __name__ == '__main__':
    app.run(debug=True)
