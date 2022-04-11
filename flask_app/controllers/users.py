from flask_app import app
from flask import render_template, redirect, request, session, Flask
from flask_app.models.user import User


@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all())

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show_user(id):
    data = {
        "id":id
    }
    return render_template("show.html", user=User.show_one(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit_user.html", user=User.show_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/users')