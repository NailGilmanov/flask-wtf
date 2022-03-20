from flask import Flask, render_template, redirect, request, abort, make_response, session
from data import db_session

from forms.user import LoginForm, RegisterForm
from data.users import User
from data.jobs import Jobs

from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)

    return render_template("index.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=f'module_{form.address}',
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


@app.route('/index/<string:title>')
def index1(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    engineer_profs = False
    if prof in ['инженер', 'строитель']:
        engineer_profs = True
    return render_template('training.html', engineer_profs=engineer_profs)


@app.route('/list_prof/<string:type>')
def list_prof(type):
    profs = [
        "инженер-исследователь",
        "пилот",
        "строитель ",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов"
    ]
    return render_template('list_prof.html',
                           type=type,
                           profs=profs)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    param = {}
    param['title'] = "first"
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе!'
    param['ready'] = 'True'
    return render_template('auto_answer.html', **param)


def main():
    db_session.global_init("db/mars_explorer.db")
    # job1 = Jobs()
    # job1.team_leader = 1
    # job1.job = 'Exploration of mineral resources'
    # job1.work_size = 25
    # job1.collaborators = '4, 3'
    # job1.is_finished = False
    #
    # job2 = Jobs()
    # job2.team_leader = 2
    # job2.job = 'Development of a management system'
    # job2.work_size = 10
    # job2.collaborators = '2'
    # job2.is_finished = True
    #
    # db_sess = db_session.create_session()
    # db_sess.add(job1)
    # db_sess.add(job2)
    # db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
