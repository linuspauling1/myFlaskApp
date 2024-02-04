from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from waitress import serve

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100))
    text = db.Column(db.String(200))

@app.route('/')
def hello_world():
    todos = Todo.query.all()
    return render_template('index.html',todos=todos)

@app.route('/post', methods=['POST'])
def add_todo():
    title = request.form['data_title']
    text  = request.form['data_text']
    if title != '' and text != '':
        new_todo = Todo(title=title, text=text)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('hello_world'))


@app.route('/delete/<int:todo_id>',methods=['POST'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0',port=5000)