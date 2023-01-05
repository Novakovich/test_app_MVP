from flask import Flask, render_template, request
from mongo_db_script import db

app = Flask(__name__)
app.debug = True


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
    user = {"name": request.form["name"], "password": request.form["password"], "email": request.form["email"]}
    users = db.users
    user_id = users.insert_one(user).inserted_id
    return render_template('create.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
