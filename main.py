from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from markupsafe import escape

from models import db, User
from forms import RegisterForm, LoginForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

app.config ['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'
crsf = CSRFProtect(app)

@app.route('/')
def index():
    return 'Hello!'

@app.cli.command('init-db')
def init_db():
    db.create_all()

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        parole = request.form.get('parole')
        if (user_name, parole) in db():
            return "Вы успешно авторизовались!"
        return f'неверный {escape(user_name)} логин и пароль'
    return render_template('login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.emil.data
        parole = form.parole.data

        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()

        if existing_user:
            error_message = 'Имя пользователя или адрес электронной почты уже существуют.'
            form.name.errors.append(error_message)
            return render_template('regist.html', form=form)
        
        user = User(name=name, email=email, parole=parole)
        user.set_parole(parole)
        db.session.add(user)
        db.session.commit()
        return 'Вы успешно зарегистрированы!'
    return render_template('regist.html', form=form)


if __name__ == 'main':
    db.create_all()
    app.run(debug=True)

