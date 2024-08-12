from flask import Flask, render_template, request, redirect, url_for

from models import db, Todo



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/todo_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)



@app.before_first_request

def create_tables():

    db.create_all()



@app.route('/')

def index():

    todos = Todo.query.all()

    return render_template('index.html', todos=todos)



@app.route('/add', methods=['POST'])

def add():

    title = request.form.get('title')

    new_todo = Todo(title=title)

    db.session.add(new_todo)

    db.session.commit()

    return redirect(url_for('index'))



@app.route('/complete/<int:todo_id>')

def complete(todo_id):

    todo = Todo.query.get_or_404(todo_id)

    todo.complete = not todo.complete

    db.session.commit()

    return redirect(url_for('index'))



@app.route('/delete/<int:todo_id>')

def delete(todo_id):

    todo = Todo.query.get_or_404(todo_id)

    db.session.delete(todo)

    db.session.commit()

    return redirect(url_for('index'))



if __name__ == '__main__':

    app.run(debug=True)

