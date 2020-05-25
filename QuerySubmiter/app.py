from flask import Flask, request, render_template, jsonify
import sqlite3
import json

app = Flask(__name__)

DB = "./chinook.db"


def get_all_users(query,json_str=False):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    db = conn.cursor()
    # db.execute("CREATE TABLE abhijeet(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    # conn.commit()


    # db.execute("INSERT INTO abhijeet VALUES(112, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    #
    # conn.commit()

    rows = db.execute(''+query+'').fetchall()

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps([dict(ix) for ix in rows])  # CREATE JSON

    return rows


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/action', methods=['GET', 'POST'])
def my_form_post():
    query = request.form['uname']
    data = get_all_users(query,json_str=True)
    data = json.loads(data)
    # columns = [i for i in data[0].keys()]
    # print(columns)
    # final_data = jsonify(data=data, columns=columns)
    # print(final_data)
    print(data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
