from flask import Flask, render_template
from data import db_session

from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)

    return render_template("index.html", jobs=jobs)


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
