from flask import Flask, render_template
from data import db_session

from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return render_template('base.html')


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
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
